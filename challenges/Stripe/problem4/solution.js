function firstMissingInteger(arr) {
    let size = arr.length;

    // set all unnecessary values to false
    // we only care about values between 1 and size, inclusive
    for (i in arr) {
        if (arr[i] < 1 || arr[i] > size) {
            arr[i] = false;
        }
    }

    // now we rearrange the input array as a boolean array
    for (i in arr) {
        if (arr[i] && typeof arr[i] == 'number') {
            markIndex(arr, arr[i]-1);
        }
    }
    
    for (i in arr) {
        if (!arr[i] || typeof arr[i] != 'boolean') {
            return Number(i)+1;
        }
    }

    return size + 1;
}

const markIndex = (arr, i) => {
    let tmp = arr[i];
    arr[i] = true;
    if (tmp && typeof tmp == 'number') {
        markIndex(arr, tmp-1);
    }
}