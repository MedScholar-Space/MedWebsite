const pdfUrl = '{{course.file.url}}';  // Replace with your PDF file path

pdfjsLib.getDocument(pdfUrl).promise.then(pdfDoc => {
    const flipbook = $('#flipbook');
    const promises = [];

    const renderPage = (pageNum) => {
        return pdfDoc.getPage(pageNum).then(page => {
            const scale = 1.5;
            const viewport = page.getViewport({ scale: scale });

            const canvas = document.createElement('canvas');
            const context = canvas.getContext('2d');
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            const renderContext = {
                canvasContext: context,
                viewport: viewport
            };

            return page.render(renderContext).promise.then(() => {
                const img = new Image();
                img.src = canvas.toDataURL();
                img.className = 'page';
                flipbook.append($('<div />').append(img));
                console.log(`Page ${pageNum} rendered and added.`);
            });
        });
    };

    // Loop through each page and render it
    for (let i = 1; i <= pdfDoc.numPages; i++) {
        promises.push(renderPage(i));
    }

    // After all pages are rendered, initialize Turn.js
document.addEventListener('DocumentContentLoaded',
Promise.all(promises).then(() => {
        console.log('All pages rendered. Initializing flipbook...');
        flipbook.turn({
            width: 800,
            height: 600,
            autoCenter: true,
            display: 'double',
            elevation: 50,
            gradients: true,
        });
    }).catch(error => {
        console.error('Error rendering pages:', error);
    }))
}).catch(error => {
    console.error('Error loading PDF:', error);
});
$(window).bind('keydown', function(e){

if (e.keyCode==37)
    $('#flipbook').turn('previous');
else if (e.keyCode==39)
    $('#flipbook').turn('next');
    
});        
