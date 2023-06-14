function dict_extend(dict1, dict2){
    for (let key in dict2){
        if(dict2.hasOwnProperty(key)){
            dict1[key] = dict2[key];
        }
    }
    return dict1;
}


function get_tr_data(tr) {
	let tr_data = {};
	let headers = $('.crud-table').find('th:not(:last)');
	tr.children(':not(:last)').each( function(i){
		let data_type = headers[i].getAttribute('id');
		tr_data[data_type] = $(this)[0].innerText;
	});
	return tr_data;
}


export function save_in_history(tr, save_mode) {
    let save = {
        'mode': save_mode,
        'timestamp': new Date().getTime() / 1000,
        'product_id': tr[0].dataset.productId
    };

    $.ajax({
        method: 'post',
        url: save_in_history_view,
        data: dict_extend(save, get_tr_data(tr)),
    });
}


export function mode_to_ru(en_mode) {
    switch (en_mode) {
        case 'create': return 'создал';
        case 'delete': return 'удалил';
        case 'update': return 'обновил';
    }
}