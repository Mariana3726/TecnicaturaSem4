const shopContent = document.getElementById("shopContent"); //busca en el html el elemento con el ID shopContent
const cart = []; //este es el carrito, un array vacío

productos.forEach((product) =>{ // con el forEach recorremos cada producto del array y lo guardamos en la variable product
    const content = document.createElement("div"); //creamos el elemento vacío
    content.className = "card";
    content.innerHTML =  ` 
        <img src="${product.img}">
        <h3>${product.productName}</h3>
        <p>${product.price} $</p>
     ` ;
    shopContent.append(content);

    const buyButton = document.createElement("button"); //creamos el elemento
    buyButton.innerText = "Comprar";

    content.append(buyButton);

    buyButton.addEventListener("click", ()=>{ //agregamos evento
        const repeat = cart.some((repeatProduct) => repeatProduct.id === product.id);

        if(repeat){
            cart.map((prod) => {
                if(prod.id === product.id){
                    prod.quanty++;
                }
            });
        }else{
            cart.push({
            id: product.id,
            productName: product.productName,
            price: product.price,
            quanty: product.quanty,
            img: product.img,
        });
    }

    });
});