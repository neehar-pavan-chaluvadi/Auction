import React, { useState } from "react";

export const Item = (props) => {
    const [name, setName] = useState('');

    return (
<div>
    {name}
</div>
    )
}