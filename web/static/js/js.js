function myFunction() {
    let search = document.getElementById('Search').value;
    let items = document.getElementById('gg').children;

    
   
    for (i = 0; i <= items.length; i++) {

     
        // console.log(bb);
        // items.style.display="block";
        items[i].style.display = "none";
        // bb.style.display="none";
        
        if (items[i].getAttribute('aa') == search) {
            items[i].style.display = "block";
          
            // bb.style.display="none";
        }
        if (search == '') {
            items[i].style.display = "block";
         
          
        }
       
        // if(search!=items[i].getAttribute('aa')){
        //     items[i].style.display = "none";
        //     bb.style.display="block";
        //     // break;
        // }
      


    }

}


let brand = document.getElementById('Brand');
brand.addEventListener('change', () => {
    let Brand = brand.value;




    let items = document.getElementById('gg').children;

    for (i = 0; i <= items.length; i++) {

        items[i].style.display = "none";

        if (items[i].getAttribute("data-id") == Brand) {
            items[i].style.transform = "3";
            items[i].style.display = "block";
        }
        if (Brand == "all") {
            items[i].style.display = "block";
        }
        
    }




})


let men=document.getElementById('M');
men.addEventListener('click',()=>{
    let aa=men.getAttribute('link');
  
    let items = document.getElementById('gg').children;
    for (i = 0; i <= items.length; i++) {

        items[i].style.display = "none";
        if(items[i].getAttribute('value')==aa){
            items[i].style.display="block";
        }
    }

})

let women=document.getElementById('W');
women.addEventListener('click',()=>{
    let aa=women.getAttribute('link');
 
    let items = document.getElementById('gg').children;
    for (i = 0; i <= items.length; i++) {

        items[i].style.display = "none";
        if(items[i].getAttribute('value')==aa){
            items[i].style.display="block";
        }
    }

})

let kid=document.getElementById('K');
kid.addEventListener('click',()=>{
    let aa=kid.getAttribute('link');
 
    let items = document.getElementById('gg').children;
    for (i = 0; i <= items.length; i++) {

        items[i].style.display = "none";
        if(items[i].getAttribute('value')==aa){
            items[i].style.display="block";
        }
    }

})

let all=document.getElementById('all');
all.addEventListener('click',()=>{
    let aa=all.getAttribute('link');
 
    let items = document.getElementById('gg').children;
    for (i = 0; i <= items.length; i++) {

        items[i].style.display = "block";
        
    }

})



    
    



