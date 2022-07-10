const app = Vue.createApp({
    data() {
        return {
            Overview: true,
            WeeklyTS: false,
        }
    
    },
    methods: {
        openOverview(){
            this.Overview = !this.Overview
        },
        openWeklyTopServices(){
            this.WeeklyTS = !this.WeeklyTS
                
        }

    }
})
app.mount('#Ihute')