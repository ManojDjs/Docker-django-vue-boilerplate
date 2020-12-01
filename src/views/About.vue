<template>
<div class="ISQ">
    
	<Chart type="radar" :data="chartData" :options="options" />
	<div class="p-col-12 p-md-6 ">Your Statistics:</div>
	
 <Button label="IMMUNE_SYS" icon="pi pi-check"  class="p-button-lg p-button-success"/>
 <Panel header="Custom Header" class="dark-panel">
 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</Panel>
    
</div>
</template>
<script>
export default {
    data() {
		return {
            options:{
                width:1000,
                height:1000

            },
			chartData: {
				labels: ['Fever', 'Diarrhea', 'HeadAch', 'Skin problems', 'Muscle and joint pain', 'Common cold', 'coughing'],
				datasets: [
					{
						label: 'ISQ 1',
						backgroundColor: 'rgba(179,181,198,0.2)',
						borderColor: '#cb4335',
						pointBackgroundColor: 'rgba(179,181,198,1)',
						pointBorderColor: '#E9967A',
						pointHoverBackgroundColor: '#fff',
						pointHoverBorderColor: 'rgba(179,181,198,1)',
						data: [1, 4, 5, 1, 5, 5, 4]
					},
					{
						label: 'ISQ 2',
						backgroundColor: 'rgba(255,99,132,0.2)',
						borderColor: ' #2874a6 ',
						pointBackgroundColor: 'rgba(255,99,132,1)',
						pointBorderColor: '#E9967A',
						pointHoverBackgroundColor: '#fff',
						pointHoverBorderColor: 'rgba(255,99,132,1)',
						data: [5, 4, 3, 5, 3, 3, 3]
					}
				]
			}
		}
	}
}
</script>

<style lang="scss" scoped>
::v-deep(.dark-panel) {
    
        background: #ff0033;
    }


</style>