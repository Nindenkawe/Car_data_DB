const app = Vue.createApp({
    data() {
        return {
            Overview: true,
            WeeklyTS: false,
            MonthlyIncomeCharts: false,
            Einsurance: true,
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
                
        },
        openEinsurance(){
            this.Einsurance = !this.Einsurance
                
        }

    }
})
app.mount('#Ihute')