let get_data = async () => {
    let res = await axios.get("http://127.0.0.1:8000/users/")
    console.log(res.data)
}

// res.forEach((item) => {
//     const li = document.createElement("li");
//     const img = document.createElement("img");
//     const img2 = document.createElement("img");
//     const div = document.createElement("div");
//     img.setAttribute("src", "../images/nuno.png");
//     img2.setAttribute("src", "../images/nuno.png");
//     li.classList.add("list-group-item");

//     li.innerHTML = `
//         <span>
//         ${item.firstName}
//         ${item.lastName}
//         <a href="tel:${item.phone}">${item.phone}</a>
//         </span>
//     `;
//     div.append(img, img2);
//     li.append(div);
//     ul.append(li);
// })