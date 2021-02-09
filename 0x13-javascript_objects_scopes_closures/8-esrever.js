#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  let i = list.length;
  while (i > 0) {
    i--;
    newlist.push(list[i]);
  }
  return newlist;
};
