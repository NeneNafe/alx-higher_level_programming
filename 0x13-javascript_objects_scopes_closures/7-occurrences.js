#!/usr/bin/node
/**
 * returns the number of occurrences in a list
 */

exports.nbOccurences = function (list, searchElement) {
    const occurrences = list.reduce((count, currentElement) => {
        if (currentElement === searchElement) {
            return count + 1;
        } else {
            return count;
        }
    }, 0);

    return occurrences;
};
