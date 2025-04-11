
$(document).ready(function () {
	$('.accordion-trigger').on('click', function () {
	  $(this).closest("tr ").next().toggle();
	  $(this).toggleClass('active');
	});
	$('[data-toggle="tooltip"]').tooltip();
	const prices = {
	  monthly: { essential: "2,499", accelerate: "2,999", ultimate: "3,499" },
	  quarterly: { essential: "7,199", accelerate: "7,999", ultimate: "9,499" },
	  halfyearly: { essential: "13,499", accelerate: "15,999", ultimate: "17,999" },
	  annually: { essential: "15,499", accelerate: "21,999", ultimate: "29,999" }
	};

	const oldPrices = {
	  monthly: { essential: "3,499", accelerate: "3,999", ultimate: "4,499" },
	  quarterly: { essential: "7,199", accelerate: "8,499", ultimate: "10,499" },
	  halfyearly: { essential: "14,499", accelerate: "17,499", ultimate: "18,499" },
	  annually: { essential: "16,,499", accelerate: "23,499", ultimate: "30,499" }
	};

	const radioButtons = document.querySelectorAll('input[type="radio"]');
	const essentialPrice = document.getElementById('essentialPrice');
	const acceleratePrice = document.getElementById('acceleratePrice');
	const ultimatePrice = document.getElementById('ultimatePrice');
	const essentialOldPrice = document.getElementById('essentialOldPrice');
	const accelerateOldPrice = document.getElementById('accelerateOldPrice');
	const ultimateOldPrice = document.getElementById('ultimateOldPrice');
	const perTags = document.querySelectorAll('.per');

	radioButtons.forEach(radio => {
	  radio.addEventListener('change', function () {
		const selectedFrequency = this.value;
		essentialPrice.textContent = prices[selectedFrequency].essential;
		acceleratePrice.textContent = prices[selectedFrequency].accelerate;
		ultimatePrice.textContent = prices[selectedFrequency].ultimate;

		essentialOldPrice.innerHTML = `<strike>${oldPrices[selectedFrequency].essential}</strike>`;
		accelerateOldPrice.innerHTML = `<strike>${oldPrices[selectedFrequency].accelerate}</strike>`;
		ultimateOldPrice.innerHTML = `<strike>${oldPrices[selectedFrequency].ultimate}</strike>`;

		perTags.forEach(tag => {
		  if (selectedFrequency === 'monthly') {
			tag.textContent = 'per month';
		  } else if (selectedFrequency === 'quarterly') {
			tag.textContent = 'per 3 months';
		  } else if (selectedFrequency === 'halfyearly') {
			tag.textContent = 'per 6 months';
		  } else if (selectedFrequency === 'annually') {
			tag.textContent = 'per annum';
		  }
		});
	  });
	});



	const audio = {
	  ava1: [1, 3, 4],
	  ava2: [1, 3, 4],
	  ava3: [30, 10, 7],
	  avb1: [1, 2, 3],
	  avb2: [1, 3, 4],
	  avb3: [1, 3, 4],
	  avb4: [1, 3, 4]
	};

	const video = {
	  ava1: [0, 2, 3],
	  ava2: [0, 1, 4],
	  ava3: [30, 10, 7],
	  avb1: [0, 1, 2],
	  avb2: [1, 2, 3],
	  avb3: [0, 1, 4],
	  avb4: [1, 0, 4]
	};

	radioButtons.forEach(button => {
	  button.addEventListener('click', function () {
		const optionName = this.name;
		const optionValue = this.value;

		let values;
		if (optionValue === 'video' && video.hasOwnProperty(optionName)) {
		  values = video[optionName];
		} else if (optionValue === 'audio' && audio.hasOwnProperty(optionName)) {
		  values = audio[optionName];
		}

		const tdElements = this.closest('.pricing-table-list').querySelectorAll('.w-col');
		tdElements.forEach((element, index) => {
		  element.textContent = values[index];
		});
	  });
	});


  });


