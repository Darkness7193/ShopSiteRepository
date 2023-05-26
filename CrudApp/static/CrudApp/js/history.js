function dictExtend(dict1, dict2){
    for (let key in dict2){
        if(dict2.hasOwnProperty(key)){
            dict1[key] = dict2[key];
        }
    }
    return dict1;
}


function getInputsData() {
	let inputs_data = {};
	let inputs = $('.field-changer');
	inputs.each( function(){
		let name = $(this)[0].getAttribute('name');
		inputs_data[name] = $(this)[0].value;
	});
	return inputs_data;
}


export function saveInHistory(tr, saveMode) {
    let save = {
        'mode': saveMode,
        'timestamp': new Date().getTime() / 1000,
        'productId': tr[0].dataset.productId,
    };

    $.ajax({
        method: 'post',
        url: saveInHistoryView,
        data: dictExtend(save, getInputsData()),
    });
}