const ModalPedido = document.querySelector('.modalPedido')
const BtnModalPedido = document.querySelector('.BntFooter')

function Modalpedido (){
  ModalPedido.showModal()

}
BtnModalPedido.addEventListener('click',Modalpedido)


  
  
  
  const switchModal = () => {
      const modal = document.querySelector('.modal')
      const actualStyle = modal.style.display
      if(actualStyle == 'block') {
        modal.style.display = 'none'
      }
      else {
        modal.style.display = 'block'
      }
    }
    
    const btn = document.querySelector('.modalBtn')
    btn.addEventListener('click', switchModal)
    
    window.onclick = function(event) {
        const modal = document.querySelector('.modal')
      if (event.target == modal) {
        switchModal()
      }
    }

const BtnFooter = document.querySelector('.BntAdd') 
const Footer = document.querySelector('.Nav-Footer')

function Produto (){
  Footer.style.display = 'flex'

}
Footer.addEventListener('click',Produto)
  

