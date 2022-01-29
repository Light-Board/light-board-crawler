// ES5+
'use strict';

// ======================================================================== //
//                            IMPORT AREA 
// ======================================================================== //
import {log} from './common/util.js';
import {getAllFood, updateFoodClear} from './store/apis.js';


// ======================================================================== //
//                            DOM RENDER AREA 
// ======================================================================== //

const getAllFoodRender = (res) => {
    const targetDiv = document.getElementById('food-list-div');
    targetDiv.innerHTML = "";

    for (let index = 0; index < res.length; index++) {
        const is_clear = (res[index]['is_clear']) ? "먹었습니다!" : "먹어야 합니다!!"
        targetDiv.innerHTML += `
            <div class="job-box d-md-flex align-items-center justify-content-between mb-30">
                <div class="job-left my-4 d-md-flex align-items-center flex-wrap">
                    <div class="img-holder mr-md-4 mb-md-0 mb-4 mx-auto mx-md-0 d-md-none d-lg-flex">
                        JS
                    </div>
                    <div class="job-content">
                        <h5 class="text-center text-md-left">${res[index]['order']}. ${res[index]['name']}</h5>
                        <ul class="d-md-flex flex-wrap text-capitalize ff-open-sans">
                            <li class="mr-md-4">
                                <i class="zmdi zmdi-pin mr-2"></i> ${res[index]['created_by']}
                            </li>
                            <li class="mr-md-4">
                                <i class="zmdi zmdi-time mr-2"></i> ${res[index]['created_data']}
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="job-right my-4 flex-shrink-0">
                    <a target-data-order=${res[index]['order']} target-date-clear=${res[index]['is_clear']} class="food-list-clear-btn btn d-block w-100 d-sm-inline-block btn-light">
                        ${is_clear}
                    </a>
                </div>
            </div>
        `;
    }
};

// Event 추가 함수
const addClikEvent = (target) => {
    const targetList = document.querySelectorAll(`.${target}`);
    targetList.forEach((targetBtn) => {
        targetBtn.addEventListener('click', (event) => {

            event.preventDefault();
            const order = event.target.getAttribute('target-data-order');
            const isClear = !(event.target.getAttribute('target-date-clear') === 'true');
            updateFoodClear(order, isClear)
                .then((res) => {
                    log(res);
                    return res.json();
                })
                .then((res) => {
                    log(res);
                    init();
                })
                .catch((error) => {
                    console.error(error);
                })
        });
    });
}



// ======================================================================== //
//                            CALL API AND MAIN 
// ======================================================================== //

const init = () => {
    // 1. 푸드 리스트 다 가져와서 랜더링 
    getAllFood()
        .then((res) => {
            log(res);
            return res.json();
        })
        .then((res) => {
            log(res);
            getAllFoodRender(res);

            // 2. (1)로 동적으로 만들어준 해당 DOM에 이벤트 추가
            addClikEvent('food-list-clear-btn');
        })
        .catch((error) => {
            console.error(error);
        })
}

init();