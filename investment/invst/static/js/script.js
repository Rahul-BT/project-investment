console.log('Start');

const elements = {
    dfTable : document.querySelectorAll('.amount'),
    dispAmt : document.querySelector('#tot-amount'),
    date : document.querySelector("input[name='date']"),
    endDate : document.querySelector("input[name='end_date']"),
    invstTab : document.getElementById('invst-tab'),
    mfTab : document.getElementById('mf-tab'),
    dentalTab : document.getElementById('dental-tab')
};

formatNumber = (num) => {
    const n2 = num.toString(10);
    return `${n2.substr(0,n2.length-3)},${n2.substr(-3)}`;
};

init = () => {
    const today = new Date();
    if (elements.date) elements.date.value = `${today.getDate()}-${today.getMonth()+1}-${today.getFullYear()}`;
    if (elements.endDate) elements.endDate.value = `${today.getDate()}-${today.getMonth()+1}-${today.getFullYear()+1}`;

    [elements.invstTab, elements.mfTab, elements.dentalTab].forEach(el => el.classList.remove('active-tab'));
    switch (window.location.pathname) {
        case '/':
            elements.invstTab.classList.toggle('active-tab');
            break;
        case '/mf':
            elements.mfTab.classList.toggle('active-tab')
            break;
        case '/dental':
        elements.dentalTab.classList.toggle('active-tab')
        break;
    } 

};

window.addEventListener('load', () => {
    
    init();
    let sum = 0;
    if (elements.dfTable.length > 0){
        const rowArr = Array.from(elements.dfTable);
        rowArr.forEach(el => {
            sum += parseInt(el.textContent.replace(',', ''));
        });
        elements.dispAmt.textContent = 'Rs ' + formatNumber(sum);
    }


});