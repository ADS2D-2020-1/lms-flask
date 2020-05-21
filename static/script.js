const linksDeletar = document.querySelectorAll('a.remover')


for(let i = 0; i < linksDeletar.length; i++){
    let link = linksDeletar[i]

    link.addEventListener('click', function(event){
        event.preventDefault()

        let href = link.href
        let tr = link.parentElement.parentElement
        let tdNome = tr.querySelector('td')
        let curso = tdNome.innerText
        let mensagem = `Tem certeza que deseja remover o curso ${curso}?`

        if(confirm(mensagem)){
            window.open(href)
        }
    })
}