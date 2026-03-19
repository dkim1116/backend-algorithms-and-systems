// Restate: Find if a student can take all courses.
// Pattern: DFS graph traversal. Use a set to keep track of nodes visited in current path.
// Use another set if I want to optimize and avoid running duplicate traversal.
// Invariant: Keep track of nodes visited in current recursive path. Clean it up when done with traversing
// the starting node and it's neighbors.
// Action: Loop through the courses and map out in a dictionary what courses have what prerequisite.
// Loop through the dictionary and traverse through the node and its neighbors while keeping track of visiting
// and visited nodes. When a node has been visited, we can move on to the next prerequisite to traverse as we will be
// revisiting a path that we've already explored. If we are done with traversing the current prerequisite
// and its neighbors, we clear out the set as we are done with the current recursive call stack.
// Why: This works because we keep track of visited nodes and update them when needed. If we see a node
// that has already been visited, we've found a cycle in the graph so a student can't take all courses.
// If we dont, then we know we're good
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
const canFinish = (numCourses, prereqs) => {
    const visited = new Set();
    const visiting = new Set();
    const courseMap = new Array(numCourses).fill(0).map(() => []);

    for (let [course, prereq] of prereqs) {
        courseMap[course].push(prereq);
    }

    const dfs = (course) => {
        if (visited.has(course)) return true;
        if (visiting.has(course)) return false;

        visiting.add(course);

        for (let prereq of courseMap[course]) {
            if (!dfs(prereq)) return false;
        }

        visiting.delete(course);
        visited.add(course);

        return true;
    }

    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) return false;
    }

    return true;
}

// prereq -> course
const isValidCourses = (numCourses, prereqs) => {
    const courseMap = new Map();

    for (let i = 0; i < numCourses; i++) {
        courseMap.set(i, []);
    }

    for ([course, prereq] of prereqs) {
        courseMap.get(course).push(prereq);
    }

    const state = new Array(numCourses).fill(0);

    const dfs = (course) => {
        if (state[course] === 1) return false;
        if (state[course] === 2) return true;

        state[course] = 1;

        for (let prereq of courseMap.get(course)) {
            if (!dfs(prereq)) return false;
        }

        state[course] = 2;

        return true;
    }

    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) return false;
    }

    return true;
}

// course -> prereq
const isValidCourses2 = (numCourses, prereqs) => {
    const courseMap = new Map();

    for (let i = 0; i < numCourses; i++) {
        courseMap.set(i, []);
    }

    for (let [course, prereq] of prereqs) {
        courseMap.get(course).push(prereq);
    }

    const visiting = new Set();
    const visited = new Set();

    const dfs = (course) => {
        if (visiting.has(course)) return false;
        if (visited.has(course)) return true;

        visiting.add(course);

        for (let prereq of courseMap.get(course)) {
            if (!dfs(prereq)) return false;
        }

        visiting.delete(course);
        visited.add(course);

        return true;
    }

    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) return false;
    }

    return true;
}


// Kahn's
const canFinish = (numCourses, prerequisites) => {
    const graph = Array.from({ length: numCourses }, () => []);
    const inDegree = new Array(numCourses).fill(0);

    for (let [course, prereq] of prerequisites) {
        graph[prereq].push(course);
        inDegree[course]++;
    }

    const queue = [];

    for (let i = 0; i < numCourses; i++) {
        if (inDegree[i] === 0) queue.push(i);
    }

    let completed = 0;

    while (queue.length) {
        const course = queue.shift();
        completed++;

        for (let next of graph[course]) {
            inDegree[next]--;
            if (inDegree[next] === 0) queue.push(next);
        }
    }

    return completed === numCourses;
};

const canFinish2 = (numCourses, prerequisites) => {
    const graph = new Array(numCourses).fill(0).map(() => []);
    const remainingPrereqs = new Array(numCourses).fill(0);

    for (let [course, prereq] of prerequisites) {
        // This is because in DFS, we go to the end of the last prerequisite. Ex: course -> prereq -> prereq...
        // In BFS, we start with prerequisite that has no remaining dependencies
        // Then tries to see which course unlocks. so prereq -> course
        graph[prereq].push(course);
        remainingPrereqs[course]++;
    }

    const queue = [];

    for (let course = 0; course < numCourses; course++) {
        if (remainingPrereqs[course] === 0) queue.push(course);
    }

    let completedCourses = 0;

    while (queue.length) {
        const course = queue.shift();
        completedCourses++;

        for (let unlockedCourse of graph[course]) {
            remainingPrereqs[unlockedCourse]--;
            if (remainingPrereqs[unlockedCourse] === 0) queue.push(unlockedCourse);
        }
    }

    return completedCourses === numCourses;
}

// [0 = [], 1 = [], 2 = []]

// [0,1] [1, 2] [2,3]
// {0: [1]
//  1: [2]
//. 2: [3]}

const canFinishDFS = (numCourses, prerequisites) => {
    const graph = new Array(numCourses).fill(0).map(() => []);
    const state = new Array(numCourses).fill(0);

    for (let [course, prereq] of prerequisites) {
        graph[course].push(prereq);
    }

    const dfs = (course) => {
        if (state[course] === 1) return false;
        if (state[course] === 2) return true;

        state[course] = 1;

        for (let prereq of graph[course]) {
            if (!dfs(prereq)) return false;
        }

        state[course] = 2;

        return true;
    };

    for (let course = 0; course < numCourses; course++) {
        if (!dfs(course)) return false;
    }

    return true;
}