var baseUrl = new URL(document.URL);
var itens = document.getElementsByClassName("item-ordenar");

for (var i = 0; i < itens.length; i++) {
    var itemUrl = new URL(baseUrl); // Crie uma nova instância de URL para cada iteração
    itemUrl.searchParams.set("ordem", itens[i].name);
    itens[i].href = itemUrl.href;
}