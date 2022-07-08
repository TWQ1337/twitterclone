import 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css'

let app = Vue.createApp({
    delimiters: ['[[',']]'],
    data(){
        return{
            tweets: [],
            body: '',
            user: 'You',
            timestamp: 'Now'
        }
    },
    methods: {
        updateTweet(value){
            var tweet = {
                'body': value,
                'user': 'you',
                'timestamp': 'just now'
            }
            this.tweets.unshift(tweet);
        },
        submitTweet(tweet){
        console.log(this.body, this.timestamp)

        if (this.body.length > 0){
            var tweet = {
                body: tweet,
                user: 'you',
                timestamp: 'just now'
            }
            this.tweets.push(tweet);
        }
        console.log(this.tweets)
    },
    },
    template: `<submit-form />           
                <div v-for='tweet in tweets' class='card'>
                    <h5>by: [[tweet.user]]</h5>
                    <p>[[tweet.body]]<p>
                    <div>[[tweet.timestamp]]</div>
                </div>
    `,
    created(){
            let endpoint = '/api/tweets/'
            fetch(endpoint)
            .then(response=>response.json())
            .then(data=>{
                for(let index = 0; index < data.length; index++) {
                    this.tweets.push(data[index])
                }
                console.log(this.tweets)
            })
            .catch(err=>console.log(err))
        }
})

app.component('submit-form', {
    template: `
        <form @submit.prevent='handleTweet'>
            <div class="form-floating">
                <textarea class="form-control" v-model='body' id="floatingTextarea"></textarea>
                <label for="floatingTextarea">Tweet here, lol</label>
            </div>
            <button class='btn btn-primary'>submit</button>
        </form>
    `,
    data(){
        return{
            body: ''
        }
    },
    methods: {
        handleTweet(){
            //packing it into the dict
            this.$root.updateTweet(this.body)
            let postEndpoint = '/api/tweets/'
            let tokenEndpoint = '/api/token/'
            let bodyContent = this.body
            fetch(tokenEndpoint)
            .then(response=>response.json())
            .then(data=>{
            let token = data['token']
            fetch(postEndpoint, {
            method: "post",
            headers: {
            'X-CSRFToken': token,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
                },
            body: JSON.stringify({
                body: bodyContent
            })
            })
            .then(response=>{
                return response.json
            })
            .then(data=>console.log(data))
        })
            this.body = ''
    }

}
})

app.mount('#feedapp')