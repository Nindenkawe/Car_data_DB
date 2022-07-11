const app = Vue.createApp({
    data() {
        return {
            Overview: true,
            WeeklyTS: false,
            MonthlyIncomeCharts: false,
        }
    
    },
    methods: {
        openOverview(){
            this.Overview = !this.Overview
        },
        openWeklyTopServices(){
            this.WeeklyTS = !this.WeeklyTS
                
        },
        openMonthlyIncomeCharts(){
            this.MonthlyIncomeCharts = !this.MonthlyIncomeCharts
                
        }

    }
})
app.mount('#Ihute')