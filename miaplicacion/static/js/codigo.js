/*Toggle icon navbar*/

let togglebtn=document.querySelector('.togglebtn');
let nav=document.querySelector('.navlinks');
let menu = document.querySelector('#menu-icon');

menu.onclick = () =>{
    menu.classList.toggle('bx-x');
}

togglebtn.addEventListener('click',function(){
    this.classList.toggle('click');
    nav.classList.toggle('open');

});


let sections=document.querySelectorAll('section');
let navLinks=document.querySelectorAll('header nav a');

/*Para cambiar el background del header*/
window.onscroll=()=>{

    sections.forEach(sec =>{
       let top = window.scrollY;
       let offset=sec.offsetTop - 150;
       let height=sec.offsetHeight;
       let id=sec.getAttribute('id');
 
       if(top >= offset && top < offset + height){
           navLinks.forEach(links=>{
               links.classList.remove('active');
               document.querySelector('header nav a[href*='+ id +']').classList.add('active');
           });
       };
   });
 
    let header=document.querySelector(".header");
    header.classList.toggle('sticky',window.scrollY > 100);

    /*remove toggle icion and   navlinks when click navlinks link (scroll)*/ 
    menu.classList.remove('bx-x');
    nav.classList.remove('open');
 
 }












