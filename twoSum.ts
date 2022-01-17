function twoSum(number: number[], target: number): number[] {
  let copyArray: number[] = [...number];
  number.sort((a, b) => a - b);

  let left: number = 0;
  let right: number = number.length - 1;
  let middle: number = number[left] + number[right];
  while (left < right) {
    if (middle === target) {
      break;
    }
    if (middle < target) {
      left++;
    } else {
      right--;
    }
    middle = number[left] + number[right];
  }
  if (number.length > 2) {
    let rightCopy: number = copyArray.indexOf(number[right]);
    let leftCopy: number = copyArray.indexOf(number[left]);
    return [leftCopy, rightCopy];
  }
  return [left, right];
}

console.log(twoSum([3, 3], 6));
