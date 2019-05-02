const axios = require('axios')

axios.get('http://13.125.249.144:8080/ssafy/daejeon/2/posts')
    .then( res => {
        console.log(res.data.posts)
    })
