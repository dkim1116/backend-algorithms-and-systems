// •	Restate: every node must satisfy min < node.val < max based on ancestors
// •	Pattern: DFS with range bounds
// •	Invariant: current node must stay within (min, max)
// •	Action: check node in range; recurse left (min, node.val); recurse right (node.val, max)
// •	Why: ancestor bounds guarantee we catch violations anywhere in the tree

// Range limits
// const bstValidate = (node, min = -Infinity, max = Infinity) => {
//     if (!node) return true;

//     if (min >= node.val || max <= node.val) return false;

//     return bstValidate(node.left, min, node.val) && bstValidate(node.right, node.val, max);
// };

// Inorder traversal
// const isBst = (root) => {
//     const stack = [];
//     let curr = root;
//     let prev;

//     while (curr || stack.length) {
//         while (curr) {
//             stack.push(curr.left);
//             curr = curr.left;
//         }

//         curr = stack.pop();
//         if (prev !== undefined && curr.val >= prev) return false;
//         prev = curr.val;
//         curr = curr.right;
//     }


//     return true;
// };


// const isBst = (root, min = -Infinity, max = Infinity) => {
//     if (!root) return true;

//     if (root.val <= min || root.val >= max) return false;

//     return isBst(root.left, min, root.val) && isBst(root.right, root.val, max);
// };

// const isBstInorder = (root) => {
//     const stack = [];
//     let curr = root;
//     let prev;

//     while (!curr || stack.length) {
//         while (curr) {
//             stack.push(curr.left);
//             curr = curr.left;
//         }

//         curr = stack.pop();
//         if (prev && prev.val > curr.val) return false;
//         prev = curr;
//         curr = curr.right;
//     }

//     return true;
// }

const isValidBST = (node, min = -Infinity, max = Infinity) => {
    if (!node) return true;
    if (node.val <= min || node.val >= max) return false;

    return isValidBST(node.left, min, node.val) && isValidBST(node.right, node.val, max);
}

const isBst = (node, min = -Infinity, max = Infinity) => {
    if (!node) return true;
    if (node.val <= min || node.val >= max) return false;

    return isBst(node.left, min, node.val) && isBst(node.right, node.val, max);
};

const isBstInorderCheck = (root) => {
    const stack = [];
    let curr = root;
    let prev;

    while (curr || stack.length) {
        while (curr) {
            stack.push(curr);
            curr = curr.left;
        }

        curr = stack.pop();
        if (prev && curr.val < prev.val) return false;
        prev = curr.val;
        curr = curr.right;
    }

    return true;
}

const isBstInorder = (root) => {
    const stack = [];
    let curr = root;
    let prev;

    while (curr || stack.length) {
        if (curr) {
            stack.push(curr);
            curr = curr.left;
        }

        curr = stack.pop();
        if (prev && curr.val <= prev.val) return false;
        prev = curr;
        curr = curr.right;
    }

    return true;
}