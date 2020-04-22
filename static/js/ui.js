const app = new Vue({
    el: '#app',
    data: {
        results: [],
        message_input: '',
        websocket_message: '',
        websocket_logs: [],
        websocket_status: "disconnected",
    },
    methods: {
        websocket_connect() {
            this.socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");
            this.socket.onopen = () => {
                this.websocket_status = "connected";
                this.websocket_logs.push({event: "Connected to", data: 'ws://127.0.0.1:8000/ws/chat/'})
                this.socket.onmessage = ({ data }) => {
                    this.results = JSON.parse(data)
                    this.websocket_logs.push({ event: "Received message", data });
                    this.$nextTick(() => {
                        this.scrollToEnd()
                    })
                };

            };
        },
        websocket_disconnect() {
            this.socket.close();
            this.websocket_status = "disconnected";
            this.websocket_logs = [];
        },
        websocket_send_message(action = 'send_message') {
            var send_message = this.message_input;
            this.message_input = '';
            this.socket.send(
                JSON.stringify({
                    "action": action,
                    "message": send_message
                })
            );
            this.websocket_logs.push({ event: "Sent message", data: this.websocket_message });
            this.websocket_message = "";
        },
        scrollToEnd: function() {
            var container = this.$el.querySelector("#message_display");
            container.scrollTop = container.scrollHeight;
        },
    },
    mounted() {
        this.websocket_connect()
    },
});

