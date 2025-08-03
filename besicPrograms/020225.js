const inpStr = "omkar"
let revStr = ""

for(let i = inpStr.length-1;i >= 0 ;i--) {
  revStr += inpStr[i]
  if (revStr.length == inpStr.length) {
    console.log(revStr)
  }
}
