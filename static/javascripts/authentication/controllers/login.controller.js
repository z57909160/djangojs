/**
 * LoginController
 * @namespace thinkster.authentication.controllers
 */
(function () {
    'use static';

    angular
        .module('thinkster.authentication.controllers')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', '$scope', 'Authentication'];

    /**
     * @namespace LoginController
     */
    function LoginController($location, $scope, Authentication) {
        var vm = this;

        vm.login = login;

        //activate();

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf thinkster.authentication.controllers.LoginController
         */
        function activate() {
            // If the user is authenticated, they should not be here.
            if (Authentication.isAuthenticated()) {
                $location.url('/');
            }
        }

        /**
         * @name login
         * @desc Log the user in
         * @memberOf thinkster.authentication.controllers.LoginController
         */
        function login() {
            var p = Authentication.login(vm.email, vm.password);
            p.then(function(value) {
                if (value.status < 200 || value.status >299) {
                    $scope.error = value.data.message;
                }
            }, function(reason) {
                console.log("Error: " + JSON.stringify(reason));
            });
        }
    }
})();