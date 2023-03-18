#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let Occurences = 0;
  for (let o = 0; o < list.length; o++) {
    if (searchElement === list[o]) {
      Occurences++;
    }
  }
  return Occurences;
};
/** exports.nbOccurences = function (list, searchElement) {
  const filteredList = list.filter((currentElement) => currentElement === searchElement);
  return filteredList.length};**/
