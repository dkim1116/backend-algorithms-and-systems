const getLowestCommonAncestor = (root, p, q) => {
    const postOrderDfs = (node) => {
        if (!node) return null;

        if (node === p || node === q) return node;

        const leftNode = postOrderDfs(node.left);
        const rightNode = postOrderDfs(node.right);

        if (leftNode && rightNode) return node;

        return leftNode || rightNode;
    }

    return postOrderDfs(root);
}


const getLCA = (root, p, q) => {
    let foundP = false;
    let foundQ = false;
    const dfs = (node) => {
        if (!node) return null;


        const left = dfs(node.left);
        const right = dfs(node.right);

        if (node === p) foundP = true;
        if (node === q) foundQ = true;

        if (node === p || node === q) return node;
        if (left && right) return node;

        return left || right;
    }
    const lca = dfs(root);
    return foundP && foundQ ? lca : null;
}

const getLowestCA = (root, p, q) => {
    const dfs = (node) => {
        if (!node) return null;

        if (node === p || node === q) return node;

        const leftNode = dfs(node.left);
        const rightNode = dfs(node.right);

        if (leftNode && rightNode) return node;

        return leftNode || rightNode;
    }

    return dfs(node);
}