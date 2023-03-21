$(window).load(function() {

				var size = 1;
				var button = 1;
				var button_class = "gallery-header-center-right-links-current";
				var normal_size_class = "gallery-content-center-normal";
				var full_size_class = "gallery-content-center-full";
				var $container = $('#gallery-content-center');

				$container.isotope({
					itemSelector : '.project-list-2 li'
				});

				function check_button() {
					$('.gallery-header-center-right-links').removeClass(button_class);
					if (button == 1) {
						$("#filter-all").addClass(button_class);
						$("#gallery-header-center-left-title").html('All Galleries');
					}
					if (button == 2) {
						$("#filter-1").addClass(button_class);
						$("#gallery-header-center-left-title").html('1 project-gallery');
					}
					if (button == 3) {
						$("#filter-2").addClass(button_class);
						$("#gallery-header-center-left-title").html('2 project-gallery');
					}
					if (button == 4) {
						$("#filter-3").addClass(button_class);
						$("#gallery-header-center-left-title").html('3 project-gallery');
					}
					if (button == 5) {
						$("#filter-4").addClass(button_class);
						$("#gallery-header-center-left-title").html('4 project-gallery');
					}
					if (button == 6) {
						$("#filter-5").addClass(button_class);
						$("#gallery-header-center-left-title").html('5 project-gallery');
					}
					if (button == 7) {
						$("#filter-6").addClass(button_class);
						$("#gallery-header-center-left-title").html('6 project-gallery');
					}
					if (button == 8) {
						$("#filter-7").addClass(button_class);
						$("#gallery-header-center-left-title").html('7 project-gallery');
					}
					if (button == 9) {
						$("#filter-8").addClass(button_class);
						$("#gallery-header-center-left-title").html('8 project-gallery');
					}
					if (button == 10) {
						$("#filter-9").addClass(button_class);
						$("#gallery-header-center-left-title").html('9 project-gallery');
					}
					if (button == 11) {
						$("#filter-10").addClass(button_class);
						$("#gallery-header-center-left-title").html('10 project-gallery');
					}
				}

				function check_size() {
					$("#gallery-content-center").removeClass(normal_size_class).removeClass(full_size_class);
					if (size == 0) {
						$("#gallery-content-center").addClass(normal_size_class);
						$("#gallery-header-center-left-icon").html('<span class="iconb" data-icon="&#xe23a;"></span>');
					}
					if (size == 1) {
						$("#gallery-content-center").addClass(full_size_class);
						$("#gallery-header-center-left-icon").html('<span class="iconb" data-icon="&#xe23b;"></span>');
					}
					$container.isotope({
						itemSelector : '.project-list-2 li'
					});
				}


				$("#filter-all").click(function() {
					$container.isotope({
						filter : '.all'
					});
					button = 1;
					check_button();
				});
				$("#filter-1").click(function() {
					$container.isotope({
						filter : '.1'
					});
					button = 2;
					check_button();
				});
				$("#filter-2").click(function() {
					$container.isotope({
						filter : '.2'
					});
					button = 3;
					check_button();
				});
				$("#filter-3").click(function() {
					$container.isotope({
						filter : '.3'
					});
					button = 4;
					check_button();
				});
				$("#filter-4").click(function() {
					$container.isotope({
						filter : '.4'
					});
					button = 5;
					check_button();
				});$("#filter-5").click(function() {
					$container.isotope({
						filter : '.5'
					});
					button = 6;
					check_button();
				});$("#filter-6").click(function() {
					$container.isotope({
						filter : '.6'
					});
					button = 7;
					check_button();
				});$("#filter-7").click(function() {
					$container.isotope({
						filter : '.7'
					});
					button = 8;
					check_button();
				});$("#filter-8").click(function() {
					$container.isotope({
						filter : '.8'
					});
					button = 9;
					check_button();
				});$("#filter-9").click(function() {
					$container.isotope({
						filter : '.9'
					});
					button = 10;
					check_button();
				});$("#filter-10").click(function() {
					$container.isotope({
						filter : '.10'
					});
					button = 11;
					check_button();
				});
				$("#gallery-header-center-left-icon").click(function() {
					if (size == 0) {
						size = 1;
					} else if (size == 1) {
						size = 0;
					}
					check_size();
				});

				check_button();
				check_size();
			});