document.addEventListener('DOMContentLoaded', () => {
    // Tombol untuk membuka modal Cryptography
    const openModalButtons = document.querySelectorAll('.open-modal');
    // Tombol untuk membuka modal Number
    const openModalNumberButtons = document.querySelectorAll('.open-modal-number');
    // Tombol untuk menutup modal
    const closeModalButtons = document.querySelectorAll('.close-modal');
    // Modal Cryptography
    const modalCryptography = document.getElementById('modal-cryptography');
    // Modal Number
    const modalNumber = document.getElementById('modal-number');

    // Membuka modal Cryptography
    openModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            modalCryptography.classList.add('active');
        });
    });

    // Membuka modal Number
    openModalNumberButtons.forEach(button => {
        button.addEventListener('click', () => {
            modalNumber.classList.add('active');
        });
    });

        // Tombol untuk membuka modal SuperBasic
    const openModalSuperBasicButtons = document.querySelectorAll('.open-modal-superbasic');
    // Modal SuperBasic
    const modalSuperBasic = document.getElementById('modal-superbasic');

    // Membuka modal SuperBasic
    openModalSuperBasicButtons.forEach(button => {
        button.addEventListener('click', () => {
            modalSuperBasic.classList.add('active');
        });
    });

    // Menutup modal saat klik di luar konten modal
    document.addEventListener('click', (event) => {
        if (event.target.classList.contains('modal-overlay')) {
            modalSuperBasic.classList.remove('active');
        }
    });


    // Menutup semua modal
    closeModalButtons.forEach(button => {
        button.addEventListener('click', () => {
            modalCryptography.classList.remove('active');
            modalNumber.classList.remove('active');
        });
    });

    // Menutup modal saat klik di luar konten modal
    document.addEventListener('click', (event) => {
        if (event.target.classList.contains('modal-overlay')) {
            modalCryptography.classList.remove('active');
            modalNumber.classList.remove('active');
        }
    });

    // Menghilangkan pesan flash setelah 2 detik
    const flashMessages = document.querySelectorAll('.flash-messages .alert');
    flashMessages.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = 0;
            setTimeout(() => {
                alert.remove();
            }, 500); // Menunggu transisi hilang (500ms)
        }, 2000); // Pesan hilang setelah 2 detik
    });
});
