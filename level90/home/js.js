//           Promise
//               |
//            PENDING
//               |
//        -----------------
//       |               |
//  FULFILLED         REJETED
//   (resolve)         (reject)


const MyPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        const students = ["nika", "nika", "gio", "alexi"];

        const randomIndex = Math.floor(Math.random() * students.length);
        const randomName = students[randomIndex];

        if (randomName.length > 5) {
            resolve("success");
        } else {
            reject("failure");
        }
    }, 5000);
});
