const findOrder = (numCourses, prerequisites) => {
    const visiting = new Set();
    const visited = new Set();
    const courseMap = new Array(numCourses).fill(0).map(() => []);
    const result = [];

    for (let [course, prereq] of prerequisites) {
        courseMap[course].push(prereq);
    }

    const dfs = (course) => {
        if(visiting.has(course)) return false;
        if(visited.has(course)) return true;

        visiting.add(course);

        for (let neighbor of courseMap[course]) {
            if(!dfs(neighbor)) {
                visiting.delete(course);
                return false;
            }
        }
        visiting.delete(course);
        visited.add(course);

        result.push(course);
        return true;
    }

    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) return [];
    }

    return result;
};


const findOrder = (numCourses, prerequisites) => {
    const visiting = new Set();
    const visited = new Set();
    const courseMap = new Array(numCourses).fill(0).map(() => []);
    let result = [];

    for (let [course, prereq] of prerequisites) {
        courseMap[course].push(prereq);
    }

    const dfs = (course) => {
        if (visiting.has(course)) return false;
        if (visited.has(couse)) return true;

        visiting.add(course);

        for (let neighbor of courseMap[course]) {
            if (!dfs(neighbor)) return false;
        }

        visiting.delete(course);
        visited.add(course);
        result.push(course);

        return true;
    }

    for (let i = 0; i < numCourses; i++) {
        if (!dfs(i)) return [];
    }

    return result;
}

const findOrderDFS = (numCourses, prerequisites) => {
    const graph = new Array(numCourses).fill(0).map(() => []);
    const state = new Array(numCourses).fill(0);

    for (let [course, prereq] of prerequisites) {
        graph[course].push(prereq);
    }

    const order = [];

    const dfs = (course) => {
        if (state[course] === 1) return false;
        if (state[course] === 2) return true;

        state[course] = 1;

        for (let prereq of graph[course]) {
            if (!dfs(prereq)) return false;
        }

        order.push(course);
        state[course] = 2;
        return true;
    }

    for (let course = 0; course < numCourses; course++) {
        if (!dfs(course)) return [];
    }
    return order;
}

const findOrderBFS = (numCourses, prerequisites) => {
    const graph = new Array(numCourses).fill(0).map(() => []);
    const remainingPrereqs = new Array(numCourses).fill(0);

    for (let [course, prereq] of prerequisites) {
        graph[prereq].push(course);
        remainingPrereqs[course]++;
    }

    const queue = [];

    for (let course = 0; course < numCourses; course++) {
        if (remainingPrereqs[course] === 0) queue.push(course);
    }

    let completedCourses = 0;
    const order = [];

    while (queue.length) {
        const course = queue.shift();
        completedCourses++;

        order.push(course);

        for (let nextCourse of graph[course]) {
            remainingPrereqs[nextCourse]--;
            if (remainingPrereqs[nextCourse] === 0) queue.push(nextCourse);
        }
    }

    return completedCourses === numCourses ? order : [];
}