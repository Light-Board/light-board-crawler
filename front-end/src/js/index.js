// ES5+
"use strict";

// ======================================================================== //
//                            IMPORT AREA
// ======================================================================== //
import { log } from "./common/util.js";
import { getAllKeyword, getSearchResults, updateRecommend } from "./store/apis.js";

// ======================================================================== //
//                            DOM RENDER AREA
// ======================================================================== //

let current_keyword = "";

// 검색 후(키워드 클릭 후) 결과 랜더링
const getJobRender = (data) => {
  const targetDiv = document.getElementById("job-list-div");

  let renderResult = ""; // string (html)
  for (let index = 0; index < data.length; index++) {
    const { title, company, location, link, id } = data[index];

    renderResult += `
      <div class="d-style btn bgc-white my-2 py-3 shadow-sm">
          <div class="row align-items-center">
              <div class="col-12 col-md-4">
                  <h4 class="job--desc--head text-600">
                      ${title}
                  </h4>
              </div>

              <ul class="list-unstyled mb-0 col-12 col-md-4 text-dark-l1 text-90 text-left my-4 my-md-0">
                  <li>
                      <label class="job--desc">Company: </label>
                      <span>
                          <span class="text-110">${company}</span>
                      </span>
                  </li>
                  <li class="mt-25">
                      <label class="job--desc">Company Location: </label>
                      <span class="text-110">
                          ${location}
                      </span>
                  </li>

                  <li class="mt-25">
                      <a class="job--desc" href="${link}" target="_blank">See details</a>
                  </li>
              </ul>

              <div class="col-12 col-md-4 text-center">
                  <button class="btn job--recommend" target-data-id="${id}" target-data-keyword="${String(current_keyword).trim()}">
                    Recommend
                  </button>
              </div>
          </div>
      </div>
    `;
  } // end of for

  targetDiv.innerHTML = renderResult
  // 검색 후 동적으로 추가된 job list에 updateRecommend Event 추가 
  addUpdateRecommendEvent()
};

// 페이지 네이션 
const getPaginationRender = (totalCount) => {
  const pageCount = Math.ceil(totalCount / 20);
  $("#pagination-demo").twbsPagination({
    totalPages: pageCount,
    visiblePages: 5,
    prev: "‹",
    next: "›",
    first: "«",
    last: "»",
    initiateStartPageClick: false,

    onPageClick: function (event, page) {

      // 검색 액션 그대로 추가 
      getSearchResults(current_keyword, page)
        .then((res) => res.json())
        .then((res) => {
          const { data } = res;
          getJobRender(data);
        })
        .catch((error) => console.error(error));
    },
  });
};

// 키워드 버튼 클릭 함수 추기
const addKeywordBtnEvent = () => {
  const keywordBtns = document.querySelectorAll(".keyword-btn");
  keywordBtns.forEach((keywordBtn) => {
    keywordBtn.addEventListener("click", () => {
      const keyword = keywordBtn.getAttribute("data-keyword");
      searchEvent(keyword);
    });
  });
};

// 동적으로 추가된 job list에 updateRecommend Event 추가 
const addUpdateRecommendEvent = () => {
  const recommendBtns = document.querySelectorAll('.job--recommend');

  recommendBtns.forEach(recommendBtn => {
    recommendBtn.addEventListener('click', (event) => {
      const jobId = recommendBtn.getAttribute('target-data-id');
      const keyword = recommendBtn.getAttribute('target-data-keyword');
      // 1. job id, keyword 가져오기 
      updateRecommend(jobId, keyword)
        .then((res) => res.json())
        .then((res) => {
          Swal.fire('SUCCESS', `you recommended well! job id is ${res['message']}`, 'success');
        })
        .catch((error) => {
          if (String(error).includes('406')) {
            Swal.fire('ERROR', `you already recommended`, 'error');
          }
          else console.error(error);
        });
    })
  });
};

// 검색 액션 추가, Keyword 검색 이벤트 등록
const searchEvent = (keyword) => {
  if (!keyword) return;
  current_keyword = keyword;

  // 1-1. 검색 누르자 마자 로딩 창 보여주기
  document.getElementById("job-list-div").innerHTML = `
    <img src="./public/images/loading_bar_gif.gif" width="25%" />
  `;

  // 1-2. 검색 기록 가져오기, 1페이지 기준
  getSearchResults(keyword, 1)
    .then((res) => res.json())
    .then((res) => {
      const { data, total_count } = res;

      // 1-3. 가져온 데이터 랜더링 하기
      getJobRender(data);

      if (total_count > 0) {
        $(".paging-div").empty();
        $(".paging-div").append(
          '<ul id="pagination-demo" class="pagination-sm"></ul>'
        );
        // 1-4. 페이지네이션 하기 
        getPaginationRender(total_count);
      }
    })
    .catch((error) => console.error(error));
}

// ======================================================================== //
//                            CALL API AND MAIN
// ======================================================================== //

const init = () => {

  // 1. Keyword 검색 이벤트 등록
  document.getElementById("search-btn").addEventListener('click', (event) => {
    event.preventDefault();
    const keyword = $("#keyword-input").val();
    searchEvent(keyword);
  });
  document.getElementById("keyword-input").addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      const keyword = $("#keyword-input").val();
      searchEvent(keyword);
    }
  });

  // 2. 키워드 리스트 다 가져오기
  getAllKeyword()
    .then((res) => res.json())
    .then((res) => {
      const autoFillBtn = document.getElementById("keyword-options");
      const keywordBtnDiv = document.getElementById("div-keyword");
      for (let index = 0; index < res["data"]["keywords"].length; index++) {
        const keyword = res["data"]["keywords"][index];
        autoFillBtn.innerHTML += `<option value="${keyword}">`;
        keywordBtnDiv.innerHTML += `
          <input class="btn btn-success keyword-btn" type="button" data-keyword="${keyword}" value="${keyword}">
        `;
      }

      // 2-1. 가져온 키워드 리스트에 검색 이벤트 추가 
      addKeywordBtnEvent();
    })
    .catch((error) => console.error(error));
};

init();
