const vm = new Vue({
    el: '#app',
    data: {
        results: [],
        message_input: ''
    },
    mounted() {
        setInterval(() => {
            axios.get("http://127.0.0.1:8000/api/message/")
                .then(response => {
                    this.results = response.data
                })
        }, 2000);
    },
    methods: {
        get_messages() {
            axios.get("http://127.0.0.1:8000/api/message/")
                .then(response => {
                    this.results = response.data
                })
        },
        send_message() {
            send_message = this.message_input;
            this.message_input = '';
            axios.post("http://127.0.0.1:8000/api/message/", {
                type: "dir",
                message: send_message,
                user: 1,
                character: null,
                to_user: null,
                to_character: null,
                channel: null
            }).then(response => {
                axios.get("http://127.0.0.1:8000/api/message/")
                    .then(response => {
                        this.results = response.data
                    })
            })
        }
    }

});

