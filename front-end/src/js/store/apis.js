// ES5+
'use strict';

// ======================================================================== //
//                            API FETCH LIST 
// ======================================================================== //

/**
 * @description 모든 food model list 가져오기 
 * @returns res object
 */
export const getAllFood = async () => {
    const res = await fetch('http://185.162.75.92:3000/baccine', {
        method: 'GET',              // *GET, POST, PUT, DELETE, etc.
        mode: 'cors',               // no-cors, cors, *same-origin
        cache: 'no-cache',          // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow',         // manual, *follow, error
        referrer: 'no-referrer',    // no-referrer, *client
        // body: JSON.stringify(data), // body data type must match "Content-Type" headerF);
    });

    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    else return res
}



/**
 * @description 타겟 food model 먹음 상태 업데이트 
 * @param clearType
 * @returns update result - res
 */
export const updateFoodClear = async (order, isClear) => {
    const clearTypeUrl = (isClear) ? `http://185.162.75.92:3000/baccine/clear/${order}` : `http://185.162.75.92:3000/baccine/unclear/${order}`;
    const res = await fetch(`${clearTypeUrl}`, {
        method: 'PUT',              // *GET, POST, PUT, DELETE, etc.
        mode: 'cors',               // no-cors, cors, *same-origin
        cache: 'no-cache',          // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow',         // manual, *follow, error
        referrer: 'no-referrer',    // no-referrer, *client
        // body: JSON.stringify(data), // body data type must match "Content-Type" headerF);
    });

    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    else return res
}
