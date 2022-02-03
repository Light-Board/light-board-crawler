// ES5+
"use strict";

// ======================================================================== //
//                            IMPORT AREA
// ======================================================================== //
import { log } from "./common/util.js";
import { getAllKeyword, updateFoodClear } from "./store/apis.js";

// ======================================================================== //
//                            DOM RENDER AREA
// ======================================================================== //

const getJobsRender = (res) => {
  const targetDiv = document.getElementById("job-list-div");
  targetDiv.innerHTML = "";

  for (let index = 0; index < res.length; index++) {
    targetDiv.innerHTML += `
            <div class="job-box d-md-flex align-items-center justify-content-between mb-30">
                <div class="job-left my-4 d-md-flex align-items-center flex-wrap">
                    <div class="img-holder mr-md-4 mb-md-0 mb-4 mx-auto mx-md-0 d-md-none d-lg-flex">
                        JS
                    </div>
                    <div class="job-content">
                        <h5 class="text-center text-md-left">${index + 1}. ${
      res[index]["title"]
    }</h5>
                        <ul class="d-md-flex flex-wrap text-capitalize ff-open-sans">
                            <li class="mr-md-4">
                                <i class="zmdi zmdi-pin mr-2"></i> ${
                                  res[index]["company"]
                                }
                            </li>
                            <li class="mr-md-4">
                                <i class="zmdi zmdi-time mr-2"></i> ${
                                  res[index]["location"]
                                }
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="job-right my-4 flex-shrink-0">
                    <a target-data-order=${
                      res[index]["order"]
                    } target-date-clear=${
      res[index]["is_clear"]
    } class="food-list-clear-btn btn d-block w-100 d-sm-inline-block btn-light">
                        따봉
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
    targetBtn.addEventListener("click", (event) => {
      event.preventDefault();
      const order = event.target.getAttribute("target-data-order");
      const isClear = !(
        event.target.getAttribute("target-date-clear") === "true"
      );
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
        });
    });
  });
};

// 키워드 버튼 클릭 함수 추기
const addKeywordBtnEvent = () => {
  const keywordBtns = document.querySelectorAll(".keyword-btn");
  keywordBtns.forEach((keywordBtn) => {
    keywordBtn.addEventListener("click", () => {
      const keyword = keywordBtn.getAttribute("data-keyword");
      window.location.href = `/api/search?keyword=${keyword}&page=1`;
    });
  });
};

// ======================================================================== //
//                            CALL API AND MAIN
// ======================================================================== //

const init = () => {
  // 1. 키워드 리스트 다 가져오기
  getAllKeyword()
    .then((res) => res.json())
    .then((res) => {
      const autoFillBtn = document.getElementById("keyword-options");
      const keywordBtnDiv = document.getElementById("div-keyword");
      for (let index = 0; index < res["data"]["keywords"].length; index++) {
        const keyword = res["data"]["keywords"][index];
        autoFillBtn.innerHTML += `
                    <option value="${keyword}">
                `;
        keywordBtnDiv.innerHTML += `
                    <input class="btn btn-success keyword-btn" type="button" data-keyword="${keyword}" value="${keyword}">
                `;
      }

      addKeywordBtnEvent();
    })
    .catch((error) => {
      console.error(error);
    });

  // 2. 초기 페이지 가져오기
  getSearchResult("python", 1)
    .then((res) => {
      log(res);
      return res.json();
    })
    .then((res) => {
      log(res);
      getJobsRender(res);

      // 2. (1)로 동적으로 만들어준 해당 DOM에 이벤트 추가
      addClikEvent("job-list-clear-btn");
    })
    .catch((error) => {
      console.error(error);
    });
};

init();
