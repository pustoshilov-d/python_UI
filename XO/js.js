
window.onload = function () {
    for (var i=0;i<3; i++) {
        for (var j = 0; j < 3; j++) {
            document.getElementById('game').innerHTML += `<div class="block" row="${i}" col="${j}"></div>`;
        }
    }

    var hod = 0;
    mass = new Array (8)
    mass = mass.fill(0);


    document.getElementById('game').onclick = function (event) {
        console.log(event.target);
        var row = parseInt(event.target.getAttribute('row')) ;
        var col = parseInt(event.target.getAttribute('col')) ;
        var mass_2 = document.getElementsByClassName("block")
        console.log(mass_2)

        if  ($(event.target).text() === ""){

            if (event.target.className =='block') {
                if (hod%2 ==0) {
                    event.target.innerHTML = 'X';
                    mass[row] += 1;
                    mass[3+row] += 1;
                    if (row ===col) {console.log(1);
                        mass[6] +=1}
                    if ((2-row) === col) {console.log(1)
                        mass[7] +=1}
                }
                hod++;
                check_finish(mass, hod)


                var elem = null;
                for (var i = 1; i<mass_2.length;i++) {
                    if ($(mass_2[i]).text() === "") {
                    elem = mass_2[i]
                    }
                }
                row = parseInt(elem.getAttribute('row')) ;
                col = parseInt(elem.getAttribute('col')) ;
                elem.innerHTML = 'O';
                mass[row] -= 1
                mass[3+row] -= 1
                if (row ===col) {
                    console.log(1)
                    mass[6] -=1}
                if ((2- row) === col) {
                    console.log(1);
                    mass[7] -=1}
                }
                hod++;
                check_finish(mass, hod)
            }
        }

        function check_finish(mass, hod){
            console.log(mass)
            if (hod === 9){
                alert('Ничья');
                document.location.reload(true)
            }
            else {
                for (var i = 0; i< mass.length; i++){
                    if (mass[i]===3){
                        alert('Пользователь победил');
                        document.location.reload(true)
                    }
                    if  (mass[i]===-3){
                        alert('Компьютер победил');
                        document.location.reload(true)
                    }

                }
            }
        }
    }
