const modalContainer = document.getElementById('tournament-modal');
const overlay = document.getElementById("overlay");

let tournamentDetail = document.querySelectorAll(".tournament-games");
tournamentDetail.forEach(function (add) {
    add.addEventListener("click", function () {
        const tournamentName = this.children[0].getAttribute("data-name");
        const tournamentBid = this.children[0].getAttribute("data-bid");
        const tournamentImage = this.children[0].getAttribute("data-img");
        const tournamentPrice = this.children[0].getAttribute("data-price");
        const tournamentDescription = this.children[0].getAttribute("data-description");
        const tournamentTutorial = this.children[0].getAttribute("data-tutorial");
        const tournamentFirstWinner = this.children[0].getAttribute("data-first");
        const tournamentSecondWinner = this.children[0].getAttribute("data-second");
        const tournamentThirdWinner = this.children[0].getAttribute("data-third");
        const tournamentOthersWinner = this.children[0].getAttribute("data-others");

        const tournament = jar.get("tournament");

        if (!tournament) {
            const data = {
                [tournamentName]: {
                    name: tournamentName,
                    bid: tournamentBid,
                    price: tournamentPrice,
                    image: tournamentImage,
                    description: tournamentDescription,
                    tutorial: tournamentTutorial,
                    first: tournamentFirstWinner,
                    second: tournamentSecondWinner,
                    third: tournamentThirdWinner,
                    others: tournamentOthersWinner,
                },
            };
            jar.set("tournament", JSON.stringify(data));
        }
        else {
            const data = {
                [tournamentName]: {
                    name: tournamentName,
                    bid: tournamentBid,
                    price: tournamentPrice,
                    image: tournamentImage,
                    description: tournamentDescription,
                    tutorial: tournamentTutorial,
                    first: tournamentFirstWinner,
                    second: tournamentSecondWinner,
                    third: tournamentThirdWinner,
                    others: tournamentOthersWinner,
                },
            };
            jar.set("tournament", JSON.stringify(data));
        }

        // Display overlay and Tournament Modal
        overlay.classList.remove("hidden");
        modalContainer.classList.remove("hidden");
        const tournamentData = JSON.parse(jar.get("tournament"));

        const parent = document.createElement("div");
        parent.className = "row justify-content-center";

        Object.keys(tournamentData).forEach((data) => {
            // cookie data variables
            const tournamentPrice = tournamentData[data].price;
            const tournamentName = tournamentData[data].name;
            const tournamentBid = tournamentData[data].bid;
            const tournamentImg = tournamentData[data].image;
            const tournamentDescription = tournamentData[data].description;
            const tournamentFirst = tournamentData[data].first;
            const tournamentSecond = tournamentData[data].second;
            const tournamentThird = tournamentData[data].third;
            const tournamentOthers = tournamentData[data].others;
            const tournamentTutorial = tournamentData[data].tutorial;

            // Modals
            const div1 = document.createElement("div")
            div1.className = "col-lg-4 col-md-6 col-12 my-5";
            const img = document.createElement("img");

            img.setAttribute("src", "/img/" + tournamentImg);
            img.className = "w-100 rounded";


            const div2 = document.createElement("div");
            div2.className = "col-lg-7 col-6 col-12 fw-semibold my-5 small";

            const div3 = document.createElement("div");
            div3.className = "row";

            const div4 = document.createElement("div");
            div4.className = "col-lg-6 col-12";

            const name = document.createElement("p");
            name.className = "display-6 fw-semibold gradient-text";
            name.innerText = tournamentName;

            const div5 = document.createElement("div");
            div5.className = "col-lg-6 col-12";

            const form = document.createElement("form");
            form.setAttribute("action", "/proceed.html");
            form.setAttribute("method", "#");

            const input1 = document.createElement("input");
            input1.setAttribute("type", "text");
            input1.setAttribute("name", "bid");
            input1.setAttribute("hidden", true);
            input1.setAttribute("value", tournamentBid);

            const input2 = document.createElement("input");
            input2.setAttribute("type", "text");
            input2.setAttribute("name", "name");
            input2.setAttribute("hidden", true);
            input2.setAttribute("value", tournamentName);

            const button = document.createElement("button");
            button.className = "btns my-3 py-1 px-5 small";
            button.innerText = "Sign In";

            const bid = document.createElement("p");
            bid.innerText = "Entry Bid : " + tournamentBid;

            const winMoney = document.createElement("p");
            winMoney.innerText = "Price Money Pool: " + tournamentPrice;

            const first = document.createElement("p");
            first.className = "ms-4 text-warning";
            first.innerText = "1ST: " + tournamentFirst + " ETB";

            const second = document.createElement("p");
            second.className = "ms-4 text-warning";
            second.innerText = "2ND: " + tournamentSecond + " ETB";

            const third = document.createElement("p");
            third.className = "ms-4 text-warning";
            third.innerText = "3RD: " + tournamentThird + " ETB";

            const others = document.createElement("p");
            others.className = "ms-4 text-warning";
            others.innerText = "4TH and UPTO 20: " + tournamentOthers + " ETB";

            const description = document.createElement("p");
            description.innerText = "Description";

            const descriptionNote = document.createElement("p");
            descriptionNote.innerText = tournamentDescription;

            const tutorial = document.createElement("p");
            tutorial.innerText = "How to Play";

            const tutorialVideo = document.createElement("video");
            tutorialVideo.setAttribute("src", "/img/Maverick.mp4");
            tutorialVideo.setAttribute("controls", "true");
            tutorialVideo.className = "w-100 pb-5";



            div1.appendChild(img);

            div2.appendChild(div3);
            div3.appendChild(div4);
            div3.appendChild(div5);

            div4.appendChild(name);
            div5.appendChild(form);
            form.appendChild(input1)
            form.appendChild(input2)
            form.appendChild(button);

            div2.appendChild(bid);
            div2.appendChild(winMoney);
            div2.appendChild(first);
            div2.appendChild(second);
            div2.appendChild(third);
            div2.appendChild(others);
            div2.appendChild(description);
            div2.appendChild(descriptionNote);
            div2.appendChild(tutorial);
            div2.appendChild(tutorialVideo);

            parent.appendChild(div1);
            parent.appendChild(div2);

            document.getElementById("tournament-modal").appendChild(parent);
        });

    });

});

overlay.addEventListener("click", () => {
    jar.remove("tournament");
    modalContainer.classList.add("hidden");
    window.location.reload();
});


const closeModalBtn = document.getElementById("close-modal");
if (closeModalBtn) {
    closeModalBtn.addEventListener("click", () => {
        jar.remove("tournament");
        modalContainer.classList.add("hidden");
        window.location.reload();
    });
}
