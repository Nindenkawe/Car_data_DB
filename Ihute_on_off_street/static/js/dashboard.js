const app = Vue.createApp({
    data() {
        return {
            Overview: true,
            ServicesOverview: true,
            MonthlyIncomeCharts: false,
            ChauffeurforHire: false,
        }
    
    },
    methods: {
        openOverview(){
            this.Overview = !this.Overview
        },
        openServicesOverview(){
            this.ServicesOverview = !this.ServicesOverview
                
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