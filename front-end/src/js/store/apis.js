// ES5+
"use strict";

// ======================================================================== //
//                            API FETCH LIST
// ======================================================================== //
const DEBUG = false;
const server_name = DEBUG
  ? "http://localhost:3000"
  : "http://nomad-crawl.kro.kr";

/**
 * @description 모든 키워드 가져오기
 * @returns res object
 */
export const getAllKeyword = async () => {
  const res = await fetch(`${server_name}/api/keyword`, {
    method: "GET", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, cors, *same-origin
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: "follow", // manual, *follow, error
    referrer: "no-referrer", // no-referrer, *client
    // body: JSON.stringify(data), // body data type must match "Content-Type" headerF);
  });

  if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
  else return res;
};


/**
 * @description Job 검새 결과 가져오기
 * @returns res object
 */
export const getSearchResults = async (keyword, page) => {
  const res = await fetch(
    `${server_name}/api/search?keyword=${keyword}&page=${page}`,
    {
      method: "GET", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, cors, *same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: "follow", // manual, *follow, error
      referrer: "no-referrer", // no-referrer, *client
      // body: JSON.stringify(data), // body data type must match "Content-Type" headerF);
    }
  );

  if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
  else return res;
};

/**
 * @description 타겟 잡 ID, keyword (query) 따봉 추가
 * @returns res object
 */
export const updateRecommend = async (jobId, keyword) => {
  const res = await fetch(
    `${server_name}/api/job/${jobId}?keyword=${keyword}`,
    {
      method: "PUT", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, cors, *same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: "follow", // manual, *follow, error
      referrer: "no-referrer", // no-referrer, *client
      // body: JSON.stringify(data), // body data type must match "Content-Type" headerF);
    }
  );

  if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
  else return res;
};
