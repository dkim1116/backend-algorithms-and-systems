const levelOrderTraversal = (root) => {
    const output = [];

    if (!root || !root.val) return output;

    const queue = [root];

    while (queue.length) {
        const queueSize = queue.length;
        const result = [];

        for (let i = 0; i < queueSize; i++) {
            const node = queue.shift();
            result.push(node.val);

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        output.push(result)
    }


    return output;
}

// Plain order traversal
const plainOrderTraversal = (root) => {
    const result = [];

    if (!root) return result;

    const queue = [root];

    while (queue.length) {
        const levelSize = queue.length;
        const level = [];

        for (let i = 0; i < levelSize; i++) {
            const node = queue.shift();

            if (node.left) {
                queue.push(node.left);
            }

            if (node.right) {
                queue.push(node.right);
            }

            level.push(node.val);
        }

        result.push(level);
    }

    return result;
}

// Traversal with extra state
const extraStateOrderTraversal = (root) => {
    if (!root) return [];

    const result = [];

    const queue = [[root, 0]]; // [node, level]

    while (queue.length) {
        const [node, level] = queue.shift();

        if (result[level] === undefined) result[level] = [];
        result[level].push(node.val);

        if (node.left) queue.push([node.left, level + 1]);
        if (node.right) queue.push([node.right, level + 1]);
    }

    return result;
}


// Optimize with not using .shift()
const optimizedPlainOrderTraversal = (root) => {
    if (!root) return [];

    const result = [];
    const queue = [root];

    let queuePointer = 0;

    while (queuePointer < queue.length) {
        const levelSize = queue.length - queuePointer;
        const level = [];

        for (let i = 0; i < levelSize; i++) {
            const node = queue[queuePointer];
            level.push(node.val);

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);

            queuePointer++;
        }

        result.push(level);
    }

    return result;
}

const optimizedExtraStateOrderTraversal = (root) => {
    if (!root) return [];

    const result = [];

    const queue = [[root, 0]]; // [node, level]
    let queuePointer = 0;

    while (queuePointer < queue.length) {
        const [node, level] = queue[queuePointer];

        if (result[level] === undefined) result[level] = [];
        result[level].push(node.val);

        if (node.left) queue.push([node.left, level + 1]);
        if (node.right) queue.push([node.right, level + 1]);
        
        queuePointer++;
    }

    return result;
}