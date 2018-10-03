import axios from 'axios'


const ax = axios.create({
  baseURL: 'http://localhost:8000',
  xsrfCookieName : "csrftoken",
  xsrfHeaderName : "X-CSRFToken",
  withCredentials : false
});


export function testApi (testFile, cb) {
  const formData = new FormData()
  formData.append('files', testFile, testFile.name)
  console.log(testFile)
  return ax.post('/test/test', formData)
    .then(function (res) {
      cb(res.data)
    }).catch(function (error) {
      console.log(error)
    })
}