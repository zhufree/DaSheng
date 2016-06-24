var url=window.location.href;//获取当前页面链接
// var cuts=url.split('/');//分隔，获取页码
// if(cuts.length<5){
// 	  var cur_page_num=1;
// }else{
// 	  var cur_page_num=parseInt(cuts[3]);
// }
function waterfall(parent, sclass) {
    var oParent = document.getElementById(parent);
    var aBox = document.getElementsByClassName(sclass);
    var boxwidth = aBox[0].offsetWidth;
    var documentwidth = window.innerWidth;
    var cnum = Math.floor(documentwidth/boxwidth);
    var aBoxHeight = [];
    for(var i = 0; i < aBox.length; i++) {
        if(i < cnum) {
            aBox[i].style.top = 0 + 'px';
            aBox[i].style.left = boxwidth * i + 'px';
            aBoxHeight.push(aBox[i].offsetHeight);
        }
        else {
            var minHeight = Math.min.apply(null, aBoxHeight);
            var minIndex = getIndex(aBoxHeight, minHeight);
            console.log(aBox[minIndex].offsetLeft);
            aBox[i].style.position = 'absolute';
            aBox[i].style.top = minHeight + 'px';
            aBox[i].style.left = aBox[minIndex].offsetLeft + 'px';
            aBoxHeight[minIndex] += aBox[i].offsetHeight;
        }
    }
}
function getIndex(arr, value) {
    for(var i in arr) {
        if(arr[i] == value) return i;
    }
}
window.onload = function() {
    console.log(window.innerWidth);
    waterfall('show-photo', 'box');
};
function checkScrollside(sClass) {
    var aBox = document.getElementsByClassName(sClass);
    var lastImgIn = aBox[aBox.length-1].offsetTop + Math.floor(aBox[aBox.length-1].offsetHeight/2);
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    var documentHeight = document.documentElement.clientHeight || document.body.clientHeight;
    return (lastImgIn < scrollTop + documentHeight);
}
// window.onscroll = function() {
//     if(checkScrollside('box')) {
//         var nexturl=cuts[0]+'//'+cuts[1]+cuts[2]+'/'+String(cur_page_num+1)+'/';
//         console.log(nexturl);
//         cur_page_num+=1;
//         var newnode=document.createElement("div");
//         newnode.setAttribute("id","new"+String(cur_page_num));
//         document.getElementById('show-photo').appendChild(newnode);
//         $('#new'+String(cur_page_num)).load(nexturl+' .box');
//         waterfall('show-photo', 'box');
//     }
// };

window.onresize = function() {
    waterfall('show-photo', 'box');
};
