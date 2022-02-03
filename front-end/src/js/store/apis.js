// ES5+
"use strict";

// ======================================================================== //
//                            API FETCH LIST
// ======================================================================== //
const server_name = "http://nomad-crawl.kro.kr";

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
 * @description 검색 결과 가져오기
 * @returns res object
 */
export const getSearchResult = async (keyword, page) => {
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
 * @description 파일 추출하기
 * @returns
 */
export const getExportFile = async (keyword, type) => {
  const res = await fetch(
    `${server_name}/api/export?keyword=${keyword}&type=${type}`,
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
