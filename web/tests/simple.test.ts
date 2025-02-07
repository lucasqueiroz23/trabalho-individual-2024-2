import { expect, test } from "vitest";

function add(a: number, b: number) {
	return a + b;
}

test("Simple check if 1 + 2 = 3", () => {
	expect(add(1, 2)).toBe(3);
});
