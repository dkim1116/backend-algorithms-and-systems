# Yelp System Design (HelloDesign Practice)

## Overview

This is my system design for a Yelp-like application.

The goal is to support:

* Searching businesses by name, category, and location
* Viewing business details and reviews
* Leaving reviews (one per user per business)

---

## Requirements

### Functional

* Search businesses (name, category, location)
* View business + reviews
* Leave reviews

### Non-Functional

* Low latency search (<500ms)
* High availability over strict consistency
* Scale to ~100M DAU and ~10M businesses

---

## High-Level Architecture

```text
Client
  ↓
API Gateway (Auth, Rate Limiting, Routing)
  ↓
-----------------------------------------
| Search Service      | Business Service |
| Review Service                         |
-----------------------------------------
  ↓
SQL Database (source of truth)
  ↓
Queue / Event Bus (Kafka / SQS)
  ↓
Indexer / Consumer
  ↓
Elasticsearch (search)
```

---

## Core Idea

I split the system into:

* **SQL (source of truth)** → correct data, transactions
* **Elasticsearch** → fast search (text + geo + ranking)

Search does NOT hit the main database.

---

## Search Flow

1. Client sends search request
2. API Gateway routes to Search Service
3. Search Service queries Elasticsearch
4. Return ranked results

Elasticsearch handles:

* full-text search (name)
* category filtering
* geo queries (distance)

---

## Business + Review Flow

### View Business

* Fetch business from DB
* Fetch reviews (paginated)

### Create Review

* Insert into Review table
* Update business aggregates (rating)
* Emit event → update Elasticsearch

---

## Data Model

### Business

* businessId
* name
* category
* latitude / longitude
* ratingSum
* reviewCount
* avgRating
* city / neighborhood (denormalized)

### Review

* reviewId
* userId
* businessId
* rating
* review
* UNIQUE(userId, businessId)

### Location

* locationId
* name (e.g. San Francisco, Mission District)
* type (city, neighborhood)
* polygon boundary

---

## Rating Calculation

Instead of recalculating on every query, I store:

* ratingSum
* reviewCount
* avgRating

On new review:

```
ratingSum += rating
reviewCount += 1
avgRating = ratingSum / reviewCount
```

This keeps reads fast and updates O(1).

---

## One Review Per User

Enforced using:

```
UNIQUE(user_id, business_id)
```

Optionally:

* use upsert if product allows edits

---

## Search Optimization

I use Elasticsearch because:

* SQL is not good for full-text search
* geo queries (distance, radius) are expensive in SQL
* ES supports ranking (relevance + rating + distance)

---

## Elasticsearch Model

Each business document:

```json
{
  "businessId": "123",
  "name": "Best Ramen",
  "category": "japanese",
  "location": {
    "lat": 37.77,
    "lon": -122.41
  },
  "rating": 4.5
}
```

`location` is stored as a `geo_point`.

---

## Search by Location Name

I maintain a predefined set of locations:

* cities
* neighborhoods

Flow:

1. User searches "Mission District"
2. Resolve to polygon boundary
3. Apply geo filter in Elasticsearch

Because the list is finite, I cache this mapping.

---

## Mapping Businesses to Locations

When a business is created:

* take lat/lon
* run point-in-polygon check against location boundaries
* assign:

  * city
  * neighborhood

This avoids recomputing on every search.

---

## Async Indexing

After DB write:

1. Publish event
2. Consumer updates Elasticsearch

This keeps search fast and decoupled.

(Optional: use transactional outbox for reliability)

---

## Tradeoffs

* Elasticsearch is eventually consistent
* Slight delay before new reviews show in search
* Acceptable due to availability + latency requirements

---

## Future Improvements

* Redis caching for hot searches
* Better ranking (rating + distance + popularity)
* Pagination using cursors instead of offset
* Sharding for large datasets
