const shopContent = document.getElementById("shopContent"); //busca en el html el elemento con el ID shopContent

productos.forEach((product) =>{ // con el forEach recorremos cada producto del array y lo guardamos en la variable product
    const content = document.createElement("div"); //creamos el elemento vacío
    content.innerHTML =  `      //define el contenido html que acabamos de crear/ la comilla para insertar valores dinámicos
    <img src="${product.img}">
    <h3>${product.productName}</h3>
    <p>${product.price} $</p>
     ` ;
    shopContent.append(content);
});