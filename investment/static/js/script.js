console.log('Start');


class Investment {
    constructor(id, date, rx, type, amt, maturity, endDate){
        this.id = id;
        
        this.date = new Date(`${date.slice(3,5)}-${date.slice(0,2)}-${date.slice(6)}`);
        this.endDate = new Date(`${endDate.slice(3,5)}-${endDate.slice(0,2)}-${endDate.slice(6)}`);
        this.rx = rx;
        this.type = type;
        this.amt = parseFloat(amt);
        this.maturity = parseFloat(maturity);
        this.months = (this.endDate.getFullYear() - this.date.getFullYear()) * 12 + this.endDate.getMonth() - this.date.getMonth();
        this.roi = (this.maturity - this.amt) / this.amt * 100;
        this.roiYear = this.roi/this.months*12;
    }
}
Investment.count = 0;


function calcSum(obj, key) {
    let sum = 0;
    for (const el1 of obj ) {
        sum += el1[key];
    }
    return sum;

}

class UIedits {
    constructor() {
        this.DOMstrings = {
            invst_table: '.invst--table',
            invst_table_row: '.invst--table--row',
            invst_sum: 'invst_sum',
            invst_return: 'invst_return',
            invst_profit: 'invst_profit',
            invst_item_add: '.item__add--btn',
            invst_item_del: '.item__delete--btn'
        };
    }

    formatAmt(num, type) {
        let numSplit, int, dec;
        if (type === 'text' || type === 'int') {
            return num;
        } else if (type === 'date'){
            return `${num.getDate()}-${num.getMonth()}-${num.getFullYear()}`;
        }

        num = Math.abs(num);
        num = num.toFixed(2);
        numSplit = num.split('.');
        if (type === 'num'){
            
            int = numSplit[0];
            if (int.length > 3) {
                int = int.substr(0, int.length - 3) + ',' + int.substr(int.length - 3, 3); //input 23510, output 23,510
            }
    
            dec = numSplit[1];
    
            return `${int}.${dec}`;
        } else if (type === 'perc') {
            return `${num}%`;
        } 

    }

    displayInvestTable(clas) {
        let html;
        const fields_1 = new Map([['id','text'], ['rx','text'], ['type','text'], ['months','int'], ['amt','num'], ['maturity','num'], ['roi','perc'], ['roiYear','perc']
                    ,['date', 'date'], ['endDate', 'date'] ]);
        html = '<tr id="invst-%id%"><td>%date%</td><td>%rx%</td><td>%type%</td><td>%amt%</td><td>%maturity%</td>'+
               '<td>%endDate%</td><td>%roi%</td><td>%months%</td><td>%roiYear%</td><td><button class="item__delete--btn"><ion-icon name="close-circle-outline">'+
               '</ion-icon></button></td></tr>';

        for(let [key, val] of fields_1) {
            html = html.replace(`%${key}%`, this.formatAmt(clas[key], val));
        }
        
        document.querySelector(this.DOMstrings.invst_table_row).insertAdjacentHTML('beforeend', html);
    }

    displayInvestSumm(sum, total, profit) {
        document.getElementById(this.DOMstrings.invst_sum).textContent = this.formatAmt(sum, 'num');
        document.getElementById(this.DOMstrings.invst_return).textContent = this.formatAmt(total, 'num');
        document.getElementById(this.DOMstrings.invst_profit).textContent = this.formatAmt(profit, 'perc');
    }
}

{
    let allInvestments = [];
    const ui = new UIedits();

    document.querySelector(ui.DOMstrings.invst_item_add).addEventListener('click', () => {
               
        const fields = document.querySelectorAll('.invst--table--input input');
        const fieldsArr = Array.prototype.slice.call(fields);

        let t = [], investSum, investReturn, investProfit;

        fieldsArr.forEach(element => {
            // console.log(element.value);
            t.push(element.value);
        });

        // Make a object
        const e1 = new Investment(Investment.count++, ...t);
        allInvestments.push(e1);
        console.log(allInvestments);

        // Display it in the UI
        ui.displayInvestTable(e1);

        // Update the Investment Summary
        investSum = calcSum(allInvestments, 'amt');
        investReturn = calcSum(allInvestments, 'maturity');
        investProfit = (investReturn - investSum) / investSum * 100;

        // Display it in the UI
        ui.displayInvestSumm(investSum, investReturn, investProfit);


        // Log it in the database
    });

    document.querySelector(ui.DOMstrings.invst_item_del).addEventListener('click', () => {
        // delete from allInvestments

        // update the investment table

        // update the investment summary

        // update the UI

    });
}