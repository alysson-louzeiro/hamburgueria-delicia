# app.py
# Este arquivo Python (Flask) serve como o backend da aplicação.
# Ele serve o arquivo HTML principal e fornece dados via API.

from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Configuração para servir arquivos estáticos (CSS, JS) e templates HTML
app.static_folder = 'static'
app.template_folder = 'templates'

# Dados de exemplo para os itens do menu
hamburgueres_data = [
    {"id": 1, "name": "Classic Burger", "description": "Carne, queijo, alface, tomate, picles e molho especial.", "price": "R$ 30,00", "image": "https://placehold.co/150x100/FF5733/FFFFFF?text=Classic+Burger"},
    {"id": 2, "name": "Chicken Burger", "description": "Frango grelhado, queijo, alface, tomate e maionese de alho.", "price": "R$ 28,00", "image": "https://placehold.co/150x100/FFC300/000000?text=Chicken+Burger"},
    {"id": 3, "name": "Veggie Burger", "description": "Hambúrguer de grão de bico, queijo vegano, rúcula e molho pesto.", "price": "R$ 32,00", "image": "https://placehold.co/150x100/90EE90/000000?text=Veggie+Burger"},
    {"id": 4, "name": "Double Cheese", "description": "Duas carnes, queijo cheddar duplo, cebola caramelizada e bacon.", "price": "R$ 38,00", "image": "https://placehold.co/150x100/FFA07A/000000?text=Double+Cheese"},
]

acompanhamentos_data = [
    {"id": 101, "name": "Batata Frita", "description": "Porção grande de batatas crocantes com sal marinho.", "price": "R$ 15,00", "image": "https://placehold.co/150x100/A78BFA/FFFFFF?text=Batata+Frita"},
    {"id": 102, "name": "Onion Rings", "description": "Anéis de cebola empanados e fritos, acompanham molho barbecue.", "price": "R$ 18,00", "image": "https://placehold.co/150x100/6A0DAD/FFFFFF?text=Onion+Rings"},
    {"id": 103, "name": "Salada da Casa", "description": "Mix de folhas, tomate cereja, pepino, cenoura e molho da casa.", "price": "R$ 20,00", "image": "https://placehold.co/150x100/ADD8E6/000000?text=Salada+Casa"},
]

bebidas_data = [
    {"id": 201, "name": "Refrigerante", "description": "Coca-cola, Pepsi, Guaraná (lata 350ml).", "price": "R$ 8,00", "image": "https://placehold.co/150x100/87CEEB/FFFFFF?text=Refrigerante"},
    {"id": 202, "name": "Suco Natural", "description": "Laranja, Abacaxi, Limão (copo 300ml).", "price": "R$ 10,00", "image": "https://placehold.co/150x100/32CD32/FFFFFF?text=Suco+Natural"},
    {"id": 203, "name": "Água Mineral", "description": "Água sem gás (500ml).", "price": "R$ 5,00", "image": "https://placehold.co/150x100/ADD8E6/000000?text=Água+Mineral"},
]

@app.route('/')
def index():
    """
    Rota principal que renderiza a página HTML.
    """
    return render_template('index.html')

@app.route('/api/menu/<category>')
def get_menu_items(category):
    """
    Endpoint da API que retorna itens do menu com base na categoria.
    """
    if category == 'hamburgueres':
        return jsonify(hamburgueres_data)
    elif category == 'acompanhamentos':
        return jsonify(acompanhamentos_data)
    elif category == 'bebidas':
        return jsonify(bebidas_data)
    else:
        return jsonify({"error": "Categoria não encontrada"}), 404

if __name__ == '__main__':
    # Cria os diretórios 'templates' e 'static' se não existirem
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    # Conteúdo do index.html
    html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hamburgueria Delícia</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/style.css">
</head>
<body class="bg-gray-50 text-gray-800 font-inter antialiased">
    <header class="bg-white shadow-md py-4 px-6 flex justify-between items-center fixed w-full top-0 z-20">
        <div class="text-2xl font-bold text-red-600">Hamburgueria</div>
        <nav class="hidden md:flex space-x-6">
            <a href="#home" class="text-gray-700 hover:text-red-600 font-medium transition duration-300">Home</a>
            <a href="#menu" class="text-gray-700 hover:text-red-600 font-medium transition duration-300">Cardápio</a>
            <a href="#about" class="text-gray-700 hover:text-red-600 font-medium transition duration-300">Sobre Nós</a>
            <a href="#contact" class="text-gray-700 hover:text-red-600 font-medium transition duration-300">Contato</a>
        </nav>
        <button id="mobileMenuButton" class="md:hidden text-gray-700 text-2xl focus:outline-none">
            &#9776; </button>
    </header>

    <nav id="mobileMenu" class="md:hidden bg-white shadow-lg fixed top-16 left-0 w-full z-10 hidden flex-col items-center py-4 space-y-4">
        <a href="#home" class="text-gray-700 hover:text-red-600 font-medium transition duration-300" onclick="toggleMobileMenu()">Home</a>
        <a href="#menu" class="text-gray-700 hover:text-red-600 font-medium transition duration-300" onclick="toggleMobileMenu()">Cardápio</a>
        <a href="#about" class="text-gray-700 hover:text-red-600 font-medium transition duration-300" onclick="toggleMobileMenu()">Sobre Nós</a>
        <a href="#contact" class="text-gray-700 hover:text-red-600 font-medium transition duration-300" onclick="toggleMobileMenu()">Contato</a>
    </nav>

    <main class="pt-20"> <section id="home" class="relative bg-gradient-to-r from-red-600 to-red-800 text-white py-20 px-6 md:py-32 flex items-center justify-center overflow-hidden rounded-b-3xl shadow-lg">
            <div class="absolute inset-0 bg-cover bg-center opacity-30" style="background-image: url('https://placehold.co/1200x600/000000/FFFFFF?text=Fundo+de+Hambúrguer');"></div>
            <div class="relative z-10 text-center max-w-3xl">
                <h1 class="text-4xl md:text-6xl font-extrabold leading-tight mb-4 animate-fade-in-up">
                    Sabores Inesquecíveis a Cada Mordida!
                </h1>
                <p class="text-lg md:text-xl mb-8 opacity-90 animate-fade-in-up delay-100">
                    Os hambúrgueres mais suculentos e acompanhamentos perfeitos esperam por você.
                </p>
                <button class="bg-yellow-400 text-red-800 font-bold py-3 px-8 rounded-full text-lg shadow-xl hover:bg-yellow-300 transition duration-300 transform hover:scale-105 animate-fade-in-up delay-200" onclick="scrollToSection('menu')">
                    Ver Cardápio
                </button>
            </div>
        </section>

        <section id="menu" class="py-16 px-6 bg-white rounded-t-3xl -mt-8 relative z-10 shadow-inner">
            <h2 class="text-4xl font-bold text-center mb-10 text-gray-900">Nosso Cardápio</h2>

            <div class="flex justify-center space-x-4 md:space-x-8 mb-10 overflow-x-auto pb-2">
                <button class="category-button px-6 py-3 rounded-full text-lg font-semibold bg-red-100 text-red-700 hover:bg-red-200 transition duration-300 whitespace-nowrap active-category-button" data-category="hamburgueres">
                    Hambúrgueres
                </button>
                <button class="category-button px-6 py-3 rounded-full text-lg font-semibold bg-gray-100 text-gray-700 hover:bg-gray-200 transition duration-300 whitespace-nowrap" data-category="acompanhamentos">
                    Acompanhamentos
                </button>
                <button class="category-button px-6 py-3 rounded-full text-lg font-semibold bg-gray-100 text-gray-700 hover:bg-gray-200 transition duration-300 whitespace-nowrap" data-category="bebidas">
                    Bebidas
                </button>
            </div>

            <div id="menuItemsContainer" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                </div>
        </section>

        <section id="about" class="py-16 px-6 bg-gray-100">
            <h2 class="text-4xl font-bold text-center mb-10 text-gray-900">Sobre Nós</h2>
            <div class="max-w-4xl mx-auto text-center text-lg text-gray-700 leading-relaxed">
                <p class="mb-4">
                    Na Hamburgueria Delícia, acreditamos que um bom hambúrguer é mais do que uma refeição; é uma experiência. Desde 20XX, nos dedicamos a criar os hambúrgueres mais saborosos, utilizando ingredientes frescos e de alta qualidade.
                </p>
                <p>
                    Nossa paixão pela culinária nos impulsiona a inovar e a oferecer um cardápio que agrada a todos os paladares, desde os clássicos até as criações mais ousadas. Venha nos visitar e descubra seu novo hambúrguer favorito!
                </p>
            </div>
        </section>

        <section id="contact" class="py-16 px-6 bg-white rounded-t-3xl shadow-inner">
            <h2 class="text-4xl font-bold text-center mb-10 text-gray-900">Fale Conosco</h2>
            <div class="max-w-xl mx-auto">
                <form class="space-y-6">
                    <div>
                        <label for="name" class="block text-lg font-medium text-gray-700 mb-2">Nome</label>
                        <input type="text" id="name" name="name" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent transition duration-200" placeholder="Seu nome completo">
                    </div>
                    <div>
                        <label for="email" class="block text-lg font-medium text-gray-700 mb-2">E-mail</label>
                        <input type="email" id="email" name="email" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent transition duration-200" placeholder="seu.email@exemplo.com">
                    </div>
                    <div>
                        <label for="message" class="block text-lg font-medium text-gray-700 mb-2">Mensagem</label>
                        <textarea id="message" name="message" rows="5" class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent transition duration-200" placeholder="Sua mensagem..."></textarea>
                    </div>
                    <button type="submit" class="w-full bg-red-600 text-white font-bold py-3 px-6 rounded-lg shadow-md hover:bg-red-700 transition duration-300 transform hover:scale-105">
                        Enviar Mensagem
                    </button>
                </form>
            </div>
        </section>
    </main>

    <footer class="bg-gray-900 text-white py-8 px-6 text-center rounded-t-3xl">
        <div class="mb-4">
            <p>&copy; 2025 Hamburgueria Delícia. Todos os direitos reservados.</p>
        </div>
        <div class="flex justify-center space-x-6">
            <a href="#" class="text-gray-400 hover:text-white transition duration-300">Facebook</a>
            <a href="#" class="text-gray-400 hover:text-white transition duration-300">Instagram</a>
            <a href="#" class="text-gray-400 hover:text-white transition duration-300">Twitter</a>
        </div>
    </footer>

    <script src="/static/script.js"></script>
</body>
</html>
    """
    with open(os.path.join('templates', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Conteúdo do style.css
    css_content = """
/* static/style.css */
/* Estilos globais e da fonte */
body {
    font-family: 'Inter', sans-serif;
}

/* Animação de fade-in-up para elementos */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fade-in-up {
    animation: fadeInUp 0.6s ease-out forwards;
    opacity: 0; /* Começa invisível */
}

.animate-fade-in-up.delay-100 {
    animation-delay: 0.1s;
}

.animate-fade-in-up.delay-200 {
    animation-delay: 0.2s;
}

/* Estilo para o botão de categoria ativo */
.category-button.active-category-button {
    background-color: #dc2626; /* red-600 */
    color: white;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

/* Estilo para o modal customizado */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.modal-content {
    background-color: white;
    padding: 1.5rem;
    border-radius: 0.75rem; /* rounded-xl */
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* shadow-lg */
    width: 90%;
    max-width: 350px;
    text-align: center;
}
    """
    with open(os.path.join('static', 'style.css'), 'w', encoding='utf-8') as f:
        f.write(css_content)

    # Conteúdo do script.js
    js_content = """
// static/script.js
// Este arquivo JavaScript lida com a interatividade do frontend e a comunicação com a API Flask.

document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuButton = document.getElementById('mobileMenuButton');
    const mobileMenu = document.getElementById('mobileMenu');
    const categoryButtons = document.querySelectorAll('.category-button');
    const menuItemsContainer = document.getElementById('menuItemsContainer');

    // Função para alternar a visibilidade do menu mobile
    window.toggleMobileMenu = () => {
        mobileMenu.classList.toggle('hidden');
    };

    mobileMenuButton.addEventListener('click', toggleMobileMenu);

    // Função para rolar suavemente para uma seção
    window.scrollToSection = (id) => {
        const section = document.getElementById(id);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
            // Fechar o menu mobile após a rolagem, se estiver aberto
            if (!mobileMenu.classList.contains('hidden')) {
                toggleMobileMenu();
            }
        }
    };

    // Adiciona event listeners para os links de navegação do cabeçalho
    document.querySelectorAll('header nav a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            scrollToSection(targetId);
        });
    });

    // Adiciona event listeners para os links de navegação do menu mobile
    document.querySelectorAll('#mobileMenu a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            scrollToSection(targetId);
        });
    });


    // Função para buscar e renderizar itens do menu
    const fetchAndRenderMenuItems = async (category) => {
        try {
            const response = await fetch(`/api/menu/${category}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const items = await response.json();
            menuItemsContainer.innerHTML = ''; // Limpa o conteúdo existente

            items.forEach(item => {
                const itemCard = document.createElement('div');
                itemCard.className = 'bg-white rounded-xl shadow-md overflow-hidden transform hover:scale-105 transition duration-300 cursor-pointer';
                itemCard.innerHTML = `
                    <img src="${item.image}" alt="${item.name}" class="w-full h-40 object-cover">
                    <div class="p-4">
                        <h3 class="text-xl font-semibold mb-2 text-gray-900">${item.name}</h3>
                        <p class="text-gray-600 text-sm mb-3">${item.description}</p>
                        <div class="flex justify-between items-center">
                            <span class="text-red-600 font-bold text-lg">${item.price}</span>
                            <button class="bg-red-600 text-white p-2 rounded-full hover:bg-red-700 transition duration-300">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clip-rule="evenodd" />
                                </svg>
                            </button>
                        </div>
                    </div>
                `;
                // Adiciona um listener de clique para simular adição ao carrinho
                itemCard.querySelector('button').addEventListener('click', (event) => {
                    event.stopPropagation(); // Evita que o clique no botão ative o clique no card
                    showCustomModal(`"${item.name}" adicionado ao carrinho!`, null, true);
                });
                menuItemsContainer.appendChild(itemCard);
            });
        } catch (error) {
            console.error(`Erro ao buscar itens da categoria ${category}:`, error);
            showCustomModal(`Não foi possível carregar os itens de ${category}. Tente novamente mais tarde.`, null, true);
        }
    };

    // Função para exibir um modal customizado (substitui alert/confirm)
    const showCustomModal = (message, callback = null, isAlert = false) => {
        // Remove qualquer modal existente para evitar duplicação
        const existingModal = document.querySelector('.modal-overlay');
        if (existingModal) {
            existingModal.remove();
        }

        const modalOverlay = document.createElement('div');
        modalOverlay.className = 'modal-overlay'; // Estilizado em style.css

        const modalContent = document.createElement('div');
        modalContent.className = 'modal-content'; // Estilizado em style.css

        modalContent.innerHTML = `
            <p class="text-gray-800 text-lg mb-4">${message}</p>
            <div class="flex justify-center space-x-4">
                ${isAlert ? '' : '<button id="cancelButton" class="bg-gray-300 text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-400 transition duration-300">Cancelar</button>'}
                <button id="confirmButton" class="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition duration-300">${isAlert ? 'OK' : 'Confirmar'}</button>
            </div>
        `;

        modalOverlay.appendChild(modalContent);
        document.body.appendChild(modalOverlay);

        const confirmButton = document.getElementById('confirmButton');
        confirmButton.addEventListener('click', () => {
            modalOverlay.remove();
            if (callback) callback(true);
        });

        if (!isAlert) {
            const cancelButton = document.getElementById('cancelButton');
            cancelButton.addEventListener('click', () => {
                modalOverlay.remove();
                if (callback) callback(false);
            });
        }
    };

    // Adiciona event listeners aos botões de categoria
    categoryButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove a classe 'active' de todos os botões e adiciona a cor padrão
            categoryButtons.forEach(btn => {
                btn.classList.remove('active-category-button', 'bg-red-600', 'text-white');
                btn.classList.add('bg-gray-100', 'text-gray-700');
            });

            // Adiciona a classe 'active' ao botão clicado e muda a cor
            button.classList.add('active-category-button', 'bg-red-600', 'text-white');
            button.classList.remove('bg-gray-100', 'text-gray-700');

            const category = button.dataset.category;
            fetchAndRenderMenuItems(category);
        });
    });

    // Carrega os hambúrgueres por padrão ao carregar a página
    fetchAndRenderMenuItems('hamburgueres');
});
    """
    with open(os.path.join('static', 'script.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)

    # Inicia o servidor Flask
    app.run(debug=True) # debug=True para desenvolvimento, desativar em produção