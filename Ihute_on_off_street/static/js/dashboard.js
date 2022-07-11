const app = Vue.createApp({
    data() {
        return {
            Overview: true,
            WeeklyTS: false,
            MonthlyIncomeCharts: false,
            ChauffeurforHire: true,
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
        openChauffeurforHire(){
            this.ChauffeurforHire = !this.ChauffeurforHire
                
        }

    }
})
app.mount('#Ihute')