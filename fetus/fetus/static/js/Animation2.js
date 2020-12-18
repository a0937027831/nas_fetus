
// document.querySelector 獲取文檔中 "header" 的元素
/*
header.classList.toggle('CSS類',條件)
這個方法的作用就是，當myDiv元素上沒有這個CSS類時，
它就新增這個CSS類；如果myDiv元素已經有了這個CSS類，它就是刪除它。就是反轉操作
*/



window.addEventListener("scroll",function(){
    var header = document.querySelector("header");
    header.classList.toggle('sticky',window.scrollY > 0);
})


function toggle(){
    var header = document.querySelector('header');
    header.classList.toggle('active');
}


